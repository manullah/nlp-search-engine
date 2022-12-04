import nltk
from nltk.corpus import wordnet   #Import wordnet from the NLTK
import pandas as pd

# my_word = "strength"
# print("My Word : " + my_word)
# print("\n")

# Test Case 1
# synset = wordnet.synsets(my_word)
# print('Word and Type : ' + synset[0].name())
# print('Synonym of Travel is: ' + synset[0].lemmas()[0].name())
# print('The meaning of the word : ' + synset[0].definition())
# print('Example of Travel : ' + str(synset[0].examples()))
# print('\n')

# Test Case 2
# syn = list()
# ant = list()
# for synset in wordnet.synsets(my_word):
#    for lemma in synset.lemmas():
#       syn.append(lemma.name())    #add the synonyms
#       if lemma.antonyms():    #When antonyms are available, add them into the list
#         ant.append(lemma.antonyms()[0].name())
# print('Synonyms: ' + str(syn))
# print('Antonyms: ' + str(ant))
# print('\n')

# Test Case 3
# first_word = wordnet.synset("Travel.v.01")
# second_word = wordnet.synset("Walk.v.01")
# print('Similarity: ' + str(first_word.wup_similarity(second_word)))
# first_word = wordnet.synset("Good.n.01")
# second_word = wordnet.synset("zebra.n.01")
# print('Similarity: ' + str(first_word.wup_similarity(second_word)))

class Synonym:
   def getSynonyms(self, x):
      syn = list()
      for synset in wordnet.synsets(x):
         for lemma in synset.lemmas():
            syn.append(lemma.name())    #add the synonyms

      return list(set(syn))