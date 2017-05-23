# **********************************************************************************************************
# Justin Espiritu
# 5/16/2017
# Version .5
# Grabs the first 20 articles from nltk.corpus reuters, and exports the following results(top 20) to a csv file:
# most frequent words, hypernyms, hypernyms of hypernyms, synonyms, synonyms of synonyms, hypernym of synonyms, synonyms of hypernyms
# **********************************************************************************************************

import string, re, nltk, csv
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords, reuters, wordnet
from nltk import word_tokenize, FreqDist, re

#remove all numbers, punctuation, and stopwords
def removal(article):
    article = article.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(article)
    filteredWords = [w for w in tokens if not w in stopwords.words('english')]
    filteredWords = [w for w in filteredWords if not w.isdigit()]
    
    return filteredWords

#return hypernyms of all words
def hypernyms(array):
    hypernyms = []
    
    for i in array:
        wordSet = wordnet.synsets(i)
        if len(wordSet) <= 0:
            continue
        hypernym = wordSet[0].hypernyms()
        if len(hypernym) <= 0:
            continue
        hypernyms.append(hypernym[0].lemma_names())
    
    hypernyms = [w[0] for w in hypernyms]
    
    return hypernyms

#return synonyms of all words
def synonyms(array):
    synonyms = []

    for i in array:
        wordSet = wordnet.synsets(i)
        if len(wordSet) <= 0:
            continue
        synonyms.append(wordSet[0].lemma_names())

    synonyms = [w[0] for w in synonyms]

    return synonyms

#return top 15 words
def frequency(array):
    frequency = FreqDist(array)
    frequency = [w[0] for w in frequency.most_common(20)]

    return frequency

#start of main program
articles = reuters.fileids()
articles = articles[:20]

with open('results.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for i in articles:
        words = removal(reuters.raw(i))
        hyp = hypernyms(words)
        hypHyp = hypernyms(hyp)
        syn = synonyms(words)
        synSyn = synonyms(syn)
        frq = frequency(words)
        hypFrq = frequency(hyp)
        synFrq = frequency(syn)
        hypHypFrq = frequency(hypHyp)
        synSynFrq = frequency(synSyn)
        hypSyn = hypernyms(syn)
        synHyp = synonyms(hyp)
        hypSynFrq = frequency(hypSyn)
        synHypFrq = frequency(synHyp)

        writer.writerow([i.upper()])
        writer.writerow(['TOP 20 WORDS'] + frq)
        writer.writerow(['HYPERNYMS'] + hypFrq)
        writer.writerow(['HYPERNYMS OF HYPERNYMS'] + hypHypFrq)
        writer.writerow(['SYNONYMS'] + synFrq)
        writer.writerow(['SYNONYMS OF SYNONYMS'] + synSynFrq)
        writer.writerow(['HYPERNYMS OF SYNONYMS'] + hypSynFrq)
        writer.writerow(['SYNONYMS OF HYPERNYMS'] + synHypFrq)