import re, helpers
import pickle
import nltk, pickle, math, ast
from itertools import chain
import pprint
import datetime, time
# import nltk
# from email.utils import parsedate_tz

pp = pprint.PrettyPrinter(indent = 4)

#stops = nltk.corpus.stopwords.words()

dim_uni_model = pickle.load(open('dementia_unigram_model.pkl'))
control_uni_model = pickle.load(open('control_unigram_model.pkl'))


dim_model = pickle.load(open('dementia_model.pkl'))
control_model = pickle.load(open('control_model.pkl'))



total_model = {}
for x in dim_uni_model:
	if x in total_model:
		total_model[x] += dim_uni_model[x]
	else:
		total_model[x] = dim_uni_model[x]


for x in control_uni_model:
	if x in total_model:
		total_model[x] += control_uni_model[x]
	else:
		total_model[x] = control_uni_model[x]



totalControlWords = 0

for x in control_uni_model:
	totalControlWords += control_uni_model[x]

totalDimWords = 0

for x in dim_uni_model:
	totalDimWords += dim_uni_model[x]
  
# def printer(tweets):
# 	username, tweets = pickle.loads(tweets)
# 	pp.pprint(tweets[0].AsDict())
# 	print "\n"

def pct_hapexes(tweets):
	username, tweets = pickle.loads(tweets)

	tweet_text = ". ".join([x.AsDict()['text'] for x in tweets])
	tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)
	lines = tweet_text.split(". ")
	hapexes = 0
	numwords = 1
	for line in lines:
		words = nltk.word_tokenize(line.lower())
		numwords += len(words)
		for word in words:
			if word not in total_model or total_model[word] == 1:
				hapexes += 1
	return hapexes/float(numwords)

def num_hapexes(tweets):
	username, tweets = pickle.loads(tweets)

	tweet_text = ". ".join([x.AsDict()['text'] for x in tweets])
	tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)
	lines = tweet_text.split(". ")
	hapexes = 0
	numwords = 1
	for line in lines:
		words = nltk.word_tokenize(line.lower())
		numwords += len(words)
		for word in words:
			if word not in total_model or total_model[word] == 1:
				hapexes += 1
	return hapexes


def unique_bigrams(tweets):
	l = []
	username, tweets = pickle.loads(tweets)

	tweet_text = ". ".join([x.AsDict()['text'] for x in tweets])
	tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)
	lines = tweet_text.split(". ")
	for line in lines:
		words = nltk.word_tokenize(line.lower())
		bigrams = nltk.bigrams(words)
		prob = 1
		for bigram in bigrams:
			l.append(bigram)

	return len(set(l))/float(len(l))


def bigram_control(tweets):
	username, tweets = pickle.loads(tweets)
	l = []
	tweet_text = ". ".join([x.AsDict()['text'] for x in tweets])
	tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)
	lines = tweet_text.split(". ")
	for line in lines:
		words = nltk.word_tokenize(line.lower())
		bigrams = nltk.bigrams(words)
		prob = 1
		for bigram in bigrams:
			if bigram not in control_model:
				control_uni_model[bigram] = 1
				if bigram[0] not in control_uni_model:
					control_uni_model[bigram[0]] = 1
				total_with = control_uni_model[bigram[0]]
				p = control_uni_model[bigram] / float(total_with)
			prob += -1 * math.log(p)
		# prob *= len(words)
		l.append(prob)
	if l == []:
		return 0
	return sum(l)/float(len(l))

def unigram_nospam(tweets):
	username, tweets = pickle.loads(tweets)

	tweet_text = ". ".join([x.AsDict()['text'] for x in tweets])
	tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)
	lines = tweet_text.split(". ")
	l = []
	for line in lines:
		words = nltk.word_tokenize(line.lower())
		prob = 1
		for word in words:
			if word not in control_uni_model:
				control_uni_model[word] = 1
			p = control_uni_model[word] / float(totalControlWords)
			prob += -1 * math.log(p)
		# prob *= len(words)
		l.append(prob)
	if l == []:
		return 0
	return sum(l)/float(len(l))

def unigram_total(tweets):
	username, tweets = pickle.loads(tweets)
	l = []
	tweet_text = ". ".join([x.AsDict()['text'] for x in tweets])
	tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)
	lines = tweet_text.split(". ")
	for line in lines:
		words = nltk.word_tokenize(line.lower())
		prob = 1
		for word in words:
			if word not in total_model:
				total_model[word] = 1
			p = total_model[word] / (float(totalControlWords) + float(totalDimWords))
			prob += -1 * math.log(p)
		# prob *= len(words)
		l.append(prob)
	if l == []:
		return 0
	return sum(l)/float(len(l))


def unigram_spam(tweets):
	l = []
	username, tweets = pickle.loads(tweets)

	tweet_text = ". ".join([x.AsDict()['text'] for x in tweets])
	tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)
	lines = tweet_text.split(". ")

	for line in lines:
		words = nltk.word_tokenize(line.lower())
		prob = 1
		for word in words:
			if word not in dim_uni_model:
				dim_uni_model[word] = 1
			p = dim_uni_model[word] / float(totalDimWords)
			prob += -1 * math.log(p)
		# prob *= len(words)
		l.append(prob)
	if l == []:
		return 0
	return sum(l)/float(len(l))



def followers(tweets):
	username, tweets = pickle.loads(tweets)
	try:
		return tweets[0].AsDict()['user']['followers_count']
	except:
		return 0

def status_count(tweets):
	username, tweets = pickle.loads(tweets)
	try:
		return tweets[0].AsDict()['user']['statuses_count']
	except:
		return 0
def favorites(tweets):
	username, tweets = pickle.loads(tweets)
	try:
		return tweets[0].AsDict()['user']['favourites_count']
	except:
		return 0
def friends(tweets):
	username, tweets = pickle.loads(tweets)
	try:
		return tweets[0].AsDict()['user']['friends_count']
	except:
		return 0

def screen_name_len(tweets):
	username, _ = pickle.loads(tweets)

	return len(username)

def avg_favs(tweets):
	username, tweets = pickle.loads(tweets)
	favs = []
	for t in tweets:
		tw = t.AsDict()
		# print tw['favorited']
		if 'favorite_count' not in tw:
			favs.append(0)
		else:
			favs.append(tw['favorite_count'])
	return float(sum(favs))/len(favs)

def pct_favorited(tweets):
	username, tweets = pickle.loads(tweets)
	favs = []
	for t in tweets:
		tw = t.AsDict()
		# print tw['favorited']
		if 'favorite_count' not in tw:
			favs.append(False)
		else:
			favs.append(True)
	return float(favs.count(True))/len(favs)

def pct_retweeted(tweets):
	username, tweets = pickle.loads(tweets)
	favs = []
	for t in tweets:
		tw = t.AsDict()
		# print tw['favorited']
		if 'retweet_count' not in tw:
			favs.append(False)
		else:
			favs.append(True)
	return float(favs.count(True))/len(favs)


# def acct_age(tweets):
# 	username, tweets = pickle.loads(tweets)

# 	ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweets[0].AsDict()['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y')).split(' ')[0].split('-')
# 	ts = datetime.datetime(int(ts[0]), int(ts[1]), int(ts[2]))
# 	t2 = datetime.datetime.now()

# 	return -1 * (ts - t2).days

def avg_RTs(tweets):
	username, tweets = pickle.loads(tweets)
	favs = []
	for t in tweets:
		tw = t.AsDict()
		# print tw['favorited']
		if 'retweet_count' not in tw:
			favs.append(0)
		else:
			favs.append(tw['retweet_count'])
	return float(sum(favs))/len(favs)

def num_RTs(tweets):
	username, tweets = pickle.loads(tweets)

	favs = []
	for t in tweets:
		tw = t.AsDict()
		# print tw['favorited']
		favs.append('rt' in tw['text'].lower())
		
	return favs.count(True)/len(favs)

def time_diff(tweets):
	username, tweets = pickle.loads(tweets)

	ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweets[0].AsDict()['created_at'],'%a %b %d %H:%M:%S +0000 %Y')).split(' ')[0].split('-')
	t2 = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweets[-1].AsDict()['created_at'],'%a %b %d %H:%M:%S +0000 %Y')).split(' ')[0].split('-')
	ts = datetime.datetime(int(ts[0]), int(ts[1]), int(ts[2]))
	t2 = datetime.datetime(int(t2[0]), int(t2[1]), int(t2[2]))

	return (ts - t2).days

def num_hashtags(tweets):
	username, tweets = pickle.loads(tweets)
	return sum([len(x.hashtags) for x in tweets])


def num_links(tweets):
	username, tweets = pickle.loads(tweets)

	return sum([len(x.urls) for x in tweets])

def geo_enabled(tweets):
	username, tweets = pickle.loads(tweets)
	try:
		return 1 if tweets[0].AsDict()['user']['geo_enabled'] else 0
	except:
		return 0

def mentions(tweets):
	username, tweets = pickle.loads(tweets)
	t = tweets[0].AsDict()

	return len(t['user_mentions']) if 'user_mentions' in t else 0


