# -*- coding: utf-8 -*-

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version. 

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
'''

import sys
import os.path
import nltk
from nltk.corpus import wordnet


mySentence = input('Enter sentence to match: ')
#mySentence = 'God was happy about it.'
print('\nYour sentence:\n{}'.format(mySentence))

sentenceFile = 'CaptureSackBaseShort.txt'

mySyns = set()
matchedSentences = []


myWords = nltk.word_tokenize(mySentence)
for myWord in myWords:
    #print('\n** {} **'.format(myWord))
    for syn in wordnet.synsets(myWord):
        syn = syn.name()[:-5]
        #print(syn)
        mySyns.add(syn)
        

if os.path.isfile(sentenceFile):
    fileOpen = open(sentenceFile)
    data = fileOpen.read().replace('\n', ' ').replace('\r', '')
    allSentences = nltk.sent_tokenize(data)
else:
    sys.exit('No file found.')

for oneSentence in allSentences:
    print()
    print()
    print (oneSentence)
    print()
    theirSyns = set()
    simCount = 0
    simIndex = 0
    theirWords = nltk.word_tokenize(oneSentence)
    for theirWord in theirWords:
        #print('\n** {} **'.format(theirWord))
        for syn in wordnet.synsets(theirWord):
            syn = syn.name()[:-5]
            #print(syn)
            theirSyns.add(syn)

            if theirWord in myWords:
                simCount += 100
                print('WORD MATCH: {}'.format(theirWord))
                break
    
    for theirSyn in theirSyns:
        if theirSyn in mySyns:
            simCount += 1
            print('SYNONYM MATCH: {}'.format(theirSyn))
            #break
    
    simIndex = (simCount / len(theirWords)) * 100
    #print('\n{}\nIndex:{}'.format(oneSentence,simIndex))
    myTup = (oneSentence,simIndex)
    if simIndex > 0 and len(oneSentence) > 3:
        matchedSentences.append(myTup)


print('\nMatched Sentences:\n')
matchedSentences = sorted(matchedSentences, key=lambda x: x[1])
for aMatch in matchedSentences:
    print(aMatch[0])
    print('Match Index: {}\n'.format(aMatch[1]))


fileOpen.close()