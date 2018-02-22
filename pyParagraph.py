import re
import os

textFile = "paragraph.txt"

f = open(textFile,'r')

strFile = f.read()

sentences = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", strFile)
numSentences = len(sentences)
numWords = len(re.findall(r'\w+', strFile))

print("Number of Sentences: " + str(numSentences))
print("Number of Words: " + str(numWords))

numLetters = len(re.findall("[A-Za-z0-9]", strFile))

print("Average letter count: "+ str(numLetters/numWords))
print("Average sentence length: " + str(numWords/numSentences))
f.close() #Close the open text file