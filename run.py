from nytimes import nytimes
from text2cfg import text2cfg
from gen_test import print_sentences

from textblob.taggers import NLTKTagger
nltk_tagger = NLTKTagger()
print('ready to text2cfg')
blahx = text2cfg(nytimes, nltk_tagger)
print(blahx)
print('Done with text2cfg')
print('ready to print')
#print_sentences(blahx)
