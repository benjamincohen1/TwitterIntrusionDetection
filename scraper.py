import twitter, TwitterAPI
import pprint, json, pickle
import os, glob, urllib2, random
import URL
pp = pprint.PrettyPrinter(indent=4)
twapi = TwitterAPI.TwitterAPI("QBSHTvUFpOOfK6rO24EpVtobp", 
	"PEMxGvDQWp2O0FAzWFOk0lJP86D7jYzrSjpVDBkMPs6VG3B94g",
	 "1569044905-iZivFTwdzkatkhB5sa92g6azCQseZNSgjHMqqH2",
	 "6aHPZm46pB2o18b0R4dSZnyoKHiPLhnTbJEb29X16oQqZ")

api = twitter.Api(consumer_key="QBSHTvUFpOOfK6rO24EpVtobp", 
	consumer_secret="PEMxGvDQWp2O0FAzWFOk0lJP86D7jYzrSjpVDBkMPs6VG3B94g",
	access_token_key= "1569044905-iZivFTwdzkatkhB5sa92g6azCQseZNSgjHMqqH2",
	access_token_secret= "6aHPZm46pB2o18b0R4dSZnyoKHiPLhnTbJEb29X16oQqZ")
# scraped = 0

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


os.chdir('Data')
# for f in glob.glob('*.pkl'):
# 	try:
# 		
# 		# pp.pprint(statuses)
# 		f = open("USER-"+screen_name+'.pkl', 'wb')
# 		pickle.dump(info_to_pickle, f)
# 	except:
		# print "ERROR"

f = open('../sites.txt', 'a')
count = 0
while(True):
	count += 1
	try:
		# if count % 2 == 0:
		r = twapi.request('search/tweets', {'q':'click here'})
		# else:
		# 	r = twapi.request('search/tweets', {'q':'.ru'})
		print "Processing " + str(len([q for q in r])) + " tweets."

	except:
		print "Request failed"
	# scraped += len([x for x in r])
	for item in r:
			# pp.pprint(item)
			print item['text']
			urls = [x['expanded_url'] for x in item['entities']['urls']]
			# print urls
			screen_name = item['user']['screen_name']
			for u in urls:

				try:
					req = urllib2.Request(u, headers={'User-Agent' : "Magic Browser"}) 
					end = urllib2.urlopen( req )
					# print con.url
					f.write(str(end.url) + "," + str(screen_name)+"\n")
					f.flush()
					# print str(u) + " went to " + str(end.url)
					# print "Spam: " + str(URL.IsSpam(end.url))
				except:
					print "Forbidden"
			# try:
			# statuses = api.GetUserTimeline(screen_name=screen_name)
			# info_to_pickle = [item['user'], statuses]

			# failed = False
			# # except:
			# # 	failed = True
			# if not failed:
			# 	if True in [URL.IsSpam(p) for p in urls]:
			# 		os.chdir("Spam")
			# 		print "Adding Spam"
			# 		f = open("USER-"+screen_name+'.pkl', 'wb')
			# 		pickle.dump(item, f)
			# 	else:
			# 		os.chdir("NoSpam")
			# 		print "Adding NoSpam"
			# 		f = open("USER-"+screen_name+'.pkl', 'wb')
			# 		pickle.dump(item, f)
			# 	os.chdir('..')

	# r = api.request('search/tweets', {'q':' a'})
	# scraped += len([x for x in r])

	# for item in r:
	# 		fileName =  str(hash(str(item)))+'.pkl'
	# 		f = open(fileName, 'wb')
	# 		pickle.dump(item, f)

	# print "Scraped: " + str(scraped)