import re, helpers
import nltk, pickle, math, ast
from itertools import chain

stops = nltk.corpus.stopwords.words()

# dim_uni_model = pickle.load(open('dementia_unigram_model.pkl'))
# control_uni_model = pickle.load(open('control_unigram_model.pkl'))


# dim_model = pickle.load(open('dementia_model.pkl'))
# control_model = pickle.load(open('control_model.pkl'))



# total_model = {}
# for x in dim_uni_model:
# 	if x in total_model:
# 		total_model[x] += dim_uni_model[x]
# 	else:
# 		total_model[x] = dim_uni_model[x]


# for x in control_uni_model:
# 	if x in total_model:
# 		total_model[x] += control_uni_model[x]
# 	else:
# 		total_model[x] = control_uni_model[x]



# totalControlWords = 0

# for x in control_uni_model:
# 	totalControlWords += control_uni_model[x]

# totalDimWords = 0

# for x in dim_uni_model:
# 	totalDimWords += dim_uni_model[x]
  
def num_hashtags(tweets):
	username, tweets = pickle.loads(tweets)

	return sum([len(x.hashtags) for x in tweets])

def num_links(tweets):
	username, tweets = pickle.loads(tweets)

	return sum([len(x.urls) for x in tweets])

