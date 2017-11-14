from collections import Counter

from textblob import TextBlob
from textblob.taggers import PatternTagger
pattern_tagger = PatternTagger()

def text_to_pos_list(text, tagger):
	blob = TextBlob(text, pos_tagger=tagger)
	return blob.pos_tags

def pos_list_to_cfg(pos_list):
	b = {}
	for i, j in pos_list:
		b.setdefault(j, []).append(i)
	x = ''.join('{}{}'.format(key, val) for key, val in b.items())
	x = x.replace('[', ' -> ')
	x = x.replace(']', ';\n')
	x = x.replace(',', ' |')
	x = x.replace('\'', '\"')
	return x

def popular_sent_pattern(text, tagger):
	''' takes text, returns cfg representation of most popular sentence pos pattern '''
	blob = TextBlob(text, pos_tagger=tagger)
	sents = [blob.sentences[i] for i in range(len(blob.sentences))]
	sent_pos = [sents[i].pos_tags for i in range(len(sents))]
	pos_hauz = [[sent_pos[i][j][1] for j in range(len(sent_pos[i]))] 
	for i in range(len(sent_pos))]
	pos_str_hauz = [' '.join(pos_hauz[i]) for i in range(len(pos_hauz))]
	# pos_str_hauz[52]
	# 'VBP PRP IN NN DT NN NNP'
	# now find most frequent pos patterns
	"""
	pos_pattern_counter = {}
	for pattern in pos_str_hauz:
		if pattern in pos_pattern_counter:
			pos_pattern_counter[pattern] += 1
		else:
			pos_pattern_counter[pattern] = 1
	popular_patterns = sorted(pos_pattern_counter, key=pos_pattern_counter.get, reverse=True)
	return popular_patterns[0]
	"""
	c = Counter(pos_str_hauz)
	return c.most_common(1)[0][0]


def print_cfg(cfg_str, text, tagger):
	cfg = 'SENTENCE -> '
	# insert popular sent pos pattern
	cfg += popular_sent_pattern(text, tagger) + ';\n'
	cfg +=cfg_str
	cfg = cfg.replace('$', 'Z')
	return cfg

def text2cfg(text, tagger):
	y = text_to_pos_list(text, tagger)
	z = pos_list_to_cfg(y)
	cfg = print_cfg(z, text, tagger)
	return cfg

'''
	break document into sentences
	for each sentence
		get sentence.pos_tags list
		for each pos_tag tuple i in list:
			new_list.add pos_tag[i][1]

		pos_ordering = return str(pos_tag ordering) for each sentence
		add all pos_orderings to some_collection
	top ten most frequent



'''
if __name__ == '__main__':
	print(text2cfg(STORY))

