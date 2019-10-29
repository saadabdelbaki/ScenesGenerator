import re
import nltk
from nltk.parse import  RecursiveDescentParser
from nltk.tokenize import word_tokenize , PunktSentenceTokenizer, RegexpTokenizer
from nltk.words.sentences




#write the source file, dunno how to take off the special characters though
newT = open("source", "r")
tokens = word_tokenize(str(newT.read()))
tokens = str(tokens)


//tokens to create 
sentence = """ This is a slef test reco to make the sentences"""
tokens = nltk.word_tokenize(sentence)
tokens
tagged[0:6]

custom_sent_tokenizer = PunktSentenceTokenizer(tokens)

tokenized = custom_sent_tokenizer.tokenize(tokens)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as k:
        print(str(k))

process_content()
