'''
	Find most popular sentence (pos) patterns

	given text, calculate mean sentence pos pattern
'''
from textblob import TextBlob
from textblob.taggers import PatternTagger

from nytimes import nytimes

pattern_tagger = PatternTagger()
# text = ''' ... '''

def popular_sent_pattern(text, tagger):
	''' takes text, returns cfg representation of most popular sentence pos pattern '''
	blob = TextBlob(nytimes, pos_tagger=tagger)
	sents = [blob.sentences[i] for i in range(len(blob.sentences))]
	sent_pos = [sents[i].pos_tags for i in range(len(sents))]
	pos_hauz = [[sent_pos[i][j][1] for j in range(len(sent_pos[i]))] 
	for i in range(len(sent_pos))]
	pos_str_hauz = [' '.join(pos_hauz[i]) for i in range(len(pos_hauz))]
	'''
	pos_str_hauz[52]
	'VBP PRP IN NN DT NN NNP'
	'''
	# now find most frequent pos patterns
	pos_pattern_counter = {}
	for pattern in pos_str_hauz:
		if pattern in pos_pattern_counter:
			pos_pattern_counter[pattern] += 1
		else:
			pos_pattern_counter[pattern] = 1
	popular_patterns = sorted(pos_pattern_counter, key=pos_pattern_counter.get, reverse=True)
	return popular_patterns[0]

