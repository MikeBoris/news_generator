import random
from nlgen.cfg import read_cfg

#from text2cfg import text2cfg

def print_sentences(GRAMMAR):
	cfg = read_cfg(GRAMMAR)
	# take the set of all sentences generated by the given GRAMMAR, form as list
	x = list(set(cfg.permutation_values('SENTENCE')))
	print('\n' + ' '.join(random.choice(x)) + '.' + '\n')


G = '''

					SENTENCE -> NNS PRONOUN NOUN;
					
					NNS -> "EMU";
					PRONOUN -> "I" | "You";	
					
					
					VERB -> "play" | "eat" | "understand";
					NOUN -> "dogs" | "poker" | "dominos" | "spaghetti";

					

'''.strip()

H = '''
					SENTENCE -> NNS VBN NNP;

					NNS -> "Lawmakers" | "scores" | "ads" | "agents";
					VBN -> 'released' | 'purchased';
					IN -> 'of' | 'on' | 'by';
					JJ -> 'political';
					NNP -> 'Wednesday' | 'Russian';
'''.strip()


if __name__ == '__main__':
	print_sentences(H)

