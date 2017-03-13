'''
@Justin Espiritu
@version 1
#create a program that will gather synonyms of synonyms a number of times in given text
'''

import nltk, string, itertools
from nltk.corpus import stopwords, gutenberg, wordnet
from nltk import word_tokenize, FreqDist, re

#set imported text to variable
mobyDick = gutenberg.words('melville-moby_dick.txt')

#set stopWords to variable
stopWords = stopwords.words('english')

#remove any punctuations, numbers, or any stopWords
mobyDick = [''.join(w for w in s if w not in string.punctuation and w not in string.digits) for s in mobyDick]
mobyDick = [w for w in mobyDick if w]
mobyDick = [w.lower() for w in mobyDick]
mobyDick = [w for w in mobyDick if w not in stopWords]

#set FreqDist of text to variable
frq = FreqDist(mobyDick)

#create a list of synonyms *note it will be in synset format 
syn = [wordnet.synsets(w[0]) for w in frq.most_common(15)]

#repeat process to see if synonyms of synonyms are similar
for i in range(10000):
	synWords = []

	#add new synonyms to list
	for w in syn:
		x = [synset.lemma_names() for synset in w]
		synWords.extend(x)

	#format list to just be a strings
	words = list(itertools.chain.from_iterable(synWords))

	#remove all numbers or stopWords
	words = [w.lower() for w in words]
	words = [w for w in words if w not in stopWords and w not in string.digits]

	#set FreqDist of synonyms to variable
	frq = FreqDist(words)

	#create a list of synonyms *again in synset format
	syn = [wordnet.synsets(w[0]) for w in frq.most_common(15)]


#print number of samples and outcomes
print(frq)

#print top 15 synonyms 
for word, frequency in frq.most_common(15):
		print(word, ':', frequency)

'''
wordLemmas = [wordnet.synsets(w) for w in words]

hypWords = []

for synset in wordLemmas:
	x = [synset.lemma_names() for i in synset]
	hypWords.extend(x)

words = list(itertools.chain.from_iterable(hypWords))		
'''

