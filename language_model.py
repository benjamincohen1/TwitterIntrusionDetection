# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 21:07:30 2014

@author: Ben
"""

import os
import nltk
import glob
from nltk.collocations import *
from nltk import word_tokenize
from nltk.util import ngrams
import pickle, re

# trigram_measures = nltk.collocations.TrigramAssocMeasures()
def build_model():
    true_model = {}
    true_unigram_model = {}
    false_model = {}
    false_unigram_model = {}
    spam_directory = "Spam"
    not_spam = "NoSpam"
    os.chdir(spam_directory)
    for email in glob.glob("*.*"):#ITERATE THROUGH ALL DATA HERE 
        _ , tweet_text  = pickle.loads(open(email).read())
        tweet_text = ". ".join([x.AsDict()['text'] for x in tweet_text])
        tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)

        add_to_model(tweet_text, true_model)
        add_to_unigram_model(tweet_text, true_unigram_model)

    #print [f for f in true_model if true_model[f] > 10]
    os.chdir('..')

   
    os.chdir(not_spam)
    for email in glob.glob("*.*"):#ITERATE THROUGH ALL DATA HERE 
        _ , tweet_text  = pickle.loads(open(email).read())
        tweet_text = ". ".join([x.AsDict()['text'] for x in tweet_text])
        tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)

        add_to_model(tweet_text, false_model)

        add_to_unigram_model(tweet_text, false_unigram_model)


          
    #export the model
    os.chdir('..')
    pickle.dump(true_model, open('control_model.pkl', 'w'))
    pickle.dump(true_unigram_model, open('control_unigram_model.pkl', 'w'))
    pickle.dump(false_model, open('dementia_model.pkl', 'w'))
    pickle.dump(false_unigram_model, open('dementia_unigram_model.pkl', 'w'))
    # print [(f, true_model[f]) for f in true_model if true_model[f] > 2]



def add_to_model(txt, model):
    # lines = getListOfUtterances(txt)
    lines = txt.split('. ')
    for line in lines:
        words = word_tokenize(line.lower())
        trigrams = ngrams(words, 2)
        if trigrams != []:
            for t in trigrams:
                if str(t) in model:
                    model[str(t)] += 1
                else:
                    model[str(t)] = 1

                    
def add_to_unigram_model(txt, model):
    # lines = getListOfUtterances(txt)
    lines = txt.split('. ')

    for line in lines:
        line = line.lower()
        words = word_tokenize(line.lower())
        trigrams = ngrams(words, 1)
        if trigrams != []:
            for t in trigrams:
                if str(t[0]) in model:
                    model[str(t[0])] += 1
                else:
                    model[str(t[0])] = 1
                                   
                
        
      
if __name__ == '__main__':
    build_model()