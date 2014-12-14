import URL
import twitter, TwitterAPI, pprint, os, pickle, random
pp = pprint.PrettyPrinter(indent=4)

api = twitter.Api(consumer_key="QBSHTvUFpOOfK6rO24EpVtobp", 
	consumer_secret="PEMxGvDQWp2O0FAzWFOk0lJP86D7jYzrSjpVDBkMPs6VG3B94g",
	access_token_key= "1569044905-iZivFTwdzkatkhB5sa92g6azCQseZNSgjHMqqH2",
	access_token_secret= "6aHPZm46pB2o18b0R4dSZnyoKHiPLhnTbJEb29X16oQqZ")

def askUserIsSpam(screen_name, statuses):
	print screen_name + "\n"
	for status in statuses:
		print status.text


	print "\n\n\n"

	i = raw_input('Enter S for spam, N for not spam: ')
	if i.lower() == "s":
		return 1
	elif i.lower() == 'n':
		return 0
	else:
		return -1

d = {}

for line in open('sites.txt'):
	try:
		site, screen_name = line.split(',')
		screen_name = screen_name.strip()
		d[screen_name] = site
	except:
		pass

keys = d.keys()
random.shuffle(keys)
for screen_name in keys:
	# print site
	statuses = api.GetUserTimeline(screen_name=screen_name)
	info_to_pickle = [screen_name, statuses]

	failed = False
	failed = askUserIsSpam(screen_name, statuses)
	if failed == 1:
		os.chdir("Spam")
		print "Adding Spam"
		f = open("USER-"+screen_name+'.pkl', 'wb')
		pickle.dump(info_to_pickle, f)
	elif failed == 0:
		os.chdir("NoSpam")
		print "Adding NoSpam"
		f = open("USER-"+screen_name+'.pkl', 'wb')
		pickle.dump(info_to_pickle, f)
	else:
		os.chdir("NoSpam")
	os.chdir('..')

