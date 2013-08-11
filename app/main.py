import random
from nltk.tokenize import word_tokenize
import nltk, re, pprint
from nltk.corpus import conll2000
import transformations 
import aiml, urllib, sys

import commands
from nltk.corpus import stopwords
import string
from speak import speakSpeechFromText

punctuation = [',','.','?','!']

basic_grammar = "NP: {<DT>?<JJ>*<NN>}"


def get_sample_response():
	count = len(sample_responses)
	return sample_responses[random.randint(0,count-1)]

def tokenize_question(question):
	tokenized = word_tokenize(question)
	return tokenized


def get_answer(question):
	cleared_question = [word[0] for word in question]
	cleared_question = ' '.join(cleared_question)
	print "Cleared:", cleared_question
	return cleared_question

def clear_question(question):
	for sym in punctuation:
		question = question.replace(sym,'')

	return question

def connect_quoted_tokens(tokens):
	begin_quote = False
	connected_token = ""
	new_tokens = []

	for token in tokens:
		if token == "``": 
			begin_quote = True
		elif token == "''":
			begin_quote = False
			new_tokens.append(connected_token)
			connected_token = ""
		elif begin_quote:
			connected_token = "{0} {1}".format(connected_token, token)
		else:
			new_tokens.append(token)

	return new_tokens
				
def remove_punctuation(sentences):
	cleared_tokens = []

	for token in sentences:
		if token not in punctuation:
			cleared_tokens.append(token)

	return cleared_tokens



def preprocess_question(question):
	lemmatizer = nltk.WordNetLemmatizer()
	
	sentences = nltk.word_tokenize(question) 
	sentences = connect_quoted_tokens(sentences)
	sentences = remove_punctuation(sentences)
	sentences = [lemmatizer.lemmatize(word) for word in sentences]
	sentences = nltk.pos_tag(sentences)
	print "Tagged"
	print sentences
	sentences = transformations.filter_insignificant(sentences)
	print "after 1", sentences
	sentences = transformations.swap_infinitive_phrase(sentences)
	sentences = transformations.remove_stopwords(sentences)
	print "after 3", sentences

	
	return sentences 


def main(argv):

    aiml_parser = aiml.Kernel()
    aiml_parser.learn("brain.xml")
    aiml_parser.respond("LOAD AIML B")
    aiml_parser.setBotPredicate("name", "Tala")
    aiml_parser.setBotPredicate("location", "Gdansk")


    question = ""
    
    previous_question = ""
    print "Hi, How can I help you?"
    while question != "0":
    	question = raw_input("> ")
    	processed_question = preprocess_question(question)
    	print "Just left"
    	if previous_question == question:
    		print "I've just told you!"
    		continue;

    	previous_question = question	
    	pattern = get_answer(processed_question)
    	final_response = aiml_parser.respond(pattern)
    	print "Should speak:"
    	print final_response

    	if not "--no-speech" in argv:
    		speakSpeechFromText(final_response)
		



if __name__ == "__main__":
    main(sys.argv[:])	