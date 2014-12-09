import pickle
import pprint
import requests
import tldextract

pp = pprint.PrettyPrinter(indent = 4)
spamUrlSet = set([])
PopulateSpamUrlSet()

def PopulateSpamUrlSet():
    with open('dom-bl-base.txt') as f:
        for line in f:
            url = line.strip()
            if ';' in url:
                index = url.index(';')
                url = url[:index]
            spamUrlSet.add(url)

            """if contains ';' character, remove it and 
            everything after """
    print "loaded spam urls"

"""
    Input: tweeter

    abstract:
    goes through all urls of every tweet from a user
    if any of the urls are in well known spam list, returns true

    returns: true iff tweeter has sent a message containing a spam URL
"""
def isSpamTweeter(tweeter):
    numSpam = 0
    for tweet in tweeter[1]:
        for url in tweet.urls:
            urlTrail = RedirectHistory(str(url.url))
            for hist in urlTrail[1]:
                if IsSpam(hist):
                    numSpam+=1
                    print "found spam: " + hist
                else:
                    print "not spam: " + hist
    print "found " + str(numSpam) + " spam messages"

def main():

    tweeter = pickle.load(open("USER-UnaChicaHapppy.pkl", "rb"))

    isSpamTweeter(tweeter)

"""
Input:
url - string

Returns
tuple(numRedirects, allUrlsList)
"""
def RedirectHistory(url):
    r = requests.get(url)
    numRedirects = len(r.history)

    allUrls = []
    for hist in r.history:
        allUrls.append(hist.url)
        IsSpam(hist.url)

    allUrls.append(r.url)
    IsSpam(r.url)

    return (numRedirects, allUrls)

"""
Input:
url - string

Returns
    true iff url's domain is a spam domain
"""
def IsSpam(url):
    ext = tldextract.extract(url)
    domain = ext.domain + '.' + ext.suffix

    isSpam = False
    if domain in spamUrlSet:
        return True
    else:
        #make API call to google safebrowsing
        #make call to other spam service
        #if either of those return true add it to the spam set

        return False


# if __name__ == "__main__":
#     main()