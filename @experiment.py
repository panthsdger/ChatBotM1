import random
import re
import time
def sentenceStructure(sentence):
	sentList = []
	for i in sentence.split(" "):
		sentList.append(returnCategory(i))
	return sentList
def returnCategory(word):
	if isNoun(word):
		return "noun"
	if isAdjective(word):
		return "adjv"
	if isVerb(word):
		return "verb"
	if isSubject(word):
		return "subj"
	if word == "a" or word == "an" or word == "the":
		return "artc"
	if isAdverb(word):
		return "advb"
	if isPreposition(word):
		return "prep"
	return "empty"
def isNoun(wordToFind):
	target = wordToFind.lower()
	openText = open('C:/Users/Samuel/Desktop/AIchat/nouns.txt', 'r')
	textReader = openText.read().split('\n')
	for word in textReader:
		if word[1:len(word)-4].lower() == target:
			return True
	return False
def isAdjective(wordToFind):
	target = wordToFind.lower()
	openText = open('C:/Users/Samuel/Desktop/AIchat/adjectives.txt', 'r')
	textReader = openText.read().split('\n')
	for word in textReader:
		if word[1:len(word)-4].lower() == target:
			return True
	return False
def isVerb(wordToFind):
	target = wordToFind.lower()
	openText = open('C:/Users/Samuel/Desktop/AIchat/verbs.txt', 'r')
	textReader = openText.read().split('\n')
	for word in textReader:
		if word[1:len(word)-4].lower() == target:
			return True
	return False
def isSubject(wordToFind):
	target = wordToFind.lower()
	openText = open('C:/Users/Samuel/Desktop/AIchat/pronouns.txt', 'r')
	textReader = openText.read().split(' \n')
	for word in textReader:
		if word.lower() == target:
			return True
	return False
def isAdverb(wordToFind):
	target = wordToFind.lower()
	openText = open('C:/Users/Samuel/Desktop/AIchat/adverbs.txt', 'r')
	textReader = openText.read().split(' \n')
	for word in textReader:
		if word.lower() == target:
			return True
	return False
def isPreposition(wordToFind):
	target = wordToFind.lower()
	openText = open('C:/Users/Samuel/Desktop/AIchat/prepositions.txt', 'r')
	textReader = openText.read().split(' \n')
	for word in textReader:
		if word.lower() == target:
			return True
	return False
def identification(subj):
	return 0
print(sentenceStructure(input()))