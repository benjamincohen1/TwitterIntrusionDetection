import URL
for line in open('sites.txt'):
	site = line.split(',')[0]
	# print site
	print str(URL.IsSpam(site))