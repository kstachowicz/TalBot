import random
from nltk.tokenize import word_tokenize
import nltk, re, pprint
from nltk.corpus import conll2000
import transformations 

import commands

sample_responses = ["mhm", "and then what..?", "that's interesting", "tell me more :)"]

knowledge_base = {"who are you": ["I am Tala. And I'm a bot.", "And you?", "Not you business."],
				"www": ["I'm from Poland", "From home", "From internet ;)"],
				"how old are you": ["100", "200", "300"]}

punctuation = ',.?!'

basic_grammar = "NP: {<DT>?<JJ>*<NN>}"


def get_sample_response():
	count = len(sample_responses)
	return sample_responses[random.randint(0,count-1)]

def tokenize_question(question):
	tokenized = word_tokenize(question)
	return tokenized


def get_answer(question):
	tokenized_question = tokenize_question(question)
	clearified_question = transformations.remove_stopwords(tokenized_question)
	
	if question in knowledge_base:
		count = len(knowledge_base[question])
		return knowledge_base[question][random.randint(0,count-1)]
	else:
		return get_sample_response()

def clear_question(question):
	for sym in punctuation:
		question = question.replace(sym,'')

	return question


def preprocess_question(question):
	"""sentences = nltk.sent_tokenize(question)"""
	sentences = nltk.word_tokenize(question) #for sent in question]
	sentences = nltk.pos_tag(sentences) #for sent in sentences]

	print "Tagged"
	print sentences
	
	sentences = transformations.filter_insignificant(sentences)
	
	#sentences = transformations.swap_verb_phrase(sentences)
	print "after 1", sentences
	sentences = transformations.swap_infinitive_phrase(sentences)
	print "after 2", sentences
	#sentences = transformations.singularize_plurar_noun(sentences)
	sentences = transformations.remove_stopwords(sentences)
	print "after 3", sentences
	print "after 4", sentences

	commands.execute(sentences)
	
	print "NE:"
	sent = sentences 
	ne_sentences = nltk.ne_chunk(sent)
	print ne_sentences
	
	return ne_sentences #chunked
	

def main():
	question = ""
	previous_question = ""
	print "Hi, How can I help you?"
	while question != "0":
		question = raw_input()
		question2 = preprocess_question(question)
		print "Just left"
		if previous_question == question:
			print "I've just told you!"
			continue;

		previous_question = question	
		answer = get_answer(question)
		print answer



if __name__ == "__main__":
	main()	