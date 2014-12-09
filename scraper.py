import twitter
import pprint, json, pickle
import os, glob, URL
pp = pprint.PrettyPrinter(indent=4)
api = twitter.Api(consumer_key="QBSHTvUFpOOfK6rO24EpVtobp", 
	consumer_secret="PEMxGvDQWp2O0FAzWFOk0lJP86D7jYzrSjpVDBkMPs6VG3B94g",
	access_token_key= "1569044905-iZivFTwdzkatkhB5sa92g6azCQseZNSgjHMqqH2",
	access_token_secret= "6aHPZm46pB2o18b0R4dSZnyoKHiPLhnTbJEb29X16oQqZ")
# scraped = 0
os.chdir('Data')
# for f in glob.glob('*.pkl'):
# 	try:
# 		
# 		# pp.pprint(statuses)
# 		f = open("USER-"+screen_name+'.pkl', 'wb')
# 		pickle.dump(info_to_pickle, f)
# 	except:
		# print "ERROR"
while(True):
	r = api.request('search/tweets', {'q':'http'})
	# scraped += len([x for x in r])
	for item in r:
			pp.pprint(item)
			url = item[]
			screen_name = tweet['user']['screen_name']
			try:
				statuses = api.GetUserTimeline(screen_name=screen_name)
				info_to_pickle = [item['user'], statuses]

				failed = False
			except:
				failed = True
			if not failed:
				if URL.isSpam(url):
					os.chdir("Spam")
					print "Adding Spam"
					f = open("USER-"+screen_name+'.pkl', 'wb')
					pickle.dump(item, f)
				else:
					os.chdir("NoSpam")
					print "Adding NoSpam"
					f = open("USER-"+screen_name+'.pkl', 'wb')
					pickle.dump(item, f)
				os.chdir('..')

	# r = api.request('search/tweets', {'q':' a'})
	# scraped += len([x for x in r])

	# for item in r:
	# 		fileName =  str(hash(str(item)))+'.pkl'
	# 		f = open(fileName, 'wb')
	# 		pickle.dump(item, f)

	# print "Scraped: " + str(scraped)