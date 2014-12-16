import URL, glob
import twitter, TwitterAPI, pprint, os, pickle, random
pp = pprint.PrettyPrinter(indent=4)

api = twitter.Api(consumer_key="QBSHTvUFpOOfK6rO24EpVtobp", 
	consumer_secret="PEMxGvDQWp2O0FAzWFOk0lJP86D7jYzrSjpVDBkMPs6VG3B94g",
	access_token_key= "1569044905-iZivFTwdzkatkhB5sa92g6azCQseZNSgjHMqqH2",
	access_token_secret= "6aHPZm46pB2o18b0R4dSZnyoKHiPLhnTbJEb29X16oQqZ")

os.chdir("NoSpam")
for fl in glob.glob('*.pkl'):
	screen_name = fl.split('-')[1].split('.')[0]
	print screen_name
	statuses = api.GetUserTimeline(screen_name=screen_name)
	info_to_pickle = [screen_name, statuses]

	
	f = open("USER-"+screen_name+'.pkl', 'wb')
	pickle.dump(info_to_pickle, f)
	