import  os, re
import math, glob

import nltk, inspect

import features
import helpers, pickle
counter = 0

def main():
		 counter = 0
		 
		 arff = open("dim.arff", "w")
		 ben_functions = inspect.getmembers(features, inspect.isfunction)


		 feature_funcitons = [] 
		 feature_funcitons +=  list([f[1] for f in ben_functions])


		 RELATION_NAME = "spam"                                  
		 arff.write("@RELATION " + RELATION_NAME + "\n")
		 for feature in feature_funcitons:
		
						arff.write("@ATTRIBUTE " +\
		
												str(feature.__name__) + " REAL\n")  #change this if we
		
																												 #have non-real number
		
																												 #values
		
		
																										 #values
		
				###PREDEFINED USER FEATURES#######
		 arff.write("@ATTRIBUTE Spam {True, False}\n")  #ie ATTRIBUTE gender {Male, Female"}
		
		 arff.write("@DATA\n")
		
		 spam_directory = "Spam"
		 not_spam = "NoSpam"
		 os.chdir(spam_directory)
		 for email in glob.glob("*.pkl"):#ITERATE THROUGH ALL DATA HERE 
			extract_features(open(email, 'r').read(), feature_funcitons, arff, False, True)

			# extract_features(email+'.pkl', parsed_feature_funcitons, arff, False, True)  

			# res = helpers.stanford_parse(open(email).read())
			# pickle.dump(res, open(email + '.pkl', 'w'))
			# if counter % 50 == 0:
			# 	print counter 
			# counter += 1

			# os.chdir('../ControlsParsed')
			# extract_parsed_features(open(email).read(), parsed_feature_funcitons, arff, False)

			# os.chdir('../Controls')
			


		 os.chdir('../NoSpam')
		 for email in glob.glob("*.pkl"):#ITERATE THROUGH ALL DATA HERE 
			try:
				extract_features(open(email, 'r').read(), feature_funcitons, arff, True, True)
			except:
				print "Failed"
			# os.chdir('../DementiaParsed')
			# extract_parsed_features(open(email).read(), parsed_feature_funcitons, arff, True)
			# res = helpers.stanford_parse(open(email))
			# pickle.dump(res, open(email + '.pkl', 'w'))
			# # os.chdir('../Dementia')
			# if counter % 50 == 0:
			# 	print counter 
			# counter += 1
	
		
		
def extract_features(data, feature_funcitons, arff, spam, end):



		values = []
		buff = ""

		for feature in feature_funcitons:

				value = feature(data)


				values.append(value)
		if end:
			if spam:
						
						buff += (",".join([str(x) for x in values]) + ', True' + "\n")
			else:
						buff += (",".join([str(x) for x in values]) + ', False' + "\n")
		else:

					buff += (",".join([str(x) for x in values]) + ',')

		
		arff.write(buff)

	


if __name__ == "__main__":
		main()
