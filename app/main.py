import random
from nltk.tokenize import word_tokenize
import nltk, re, pprint
from nltk.corpus import conll2000
import transformations 
import aiml

import commands
from nltk.corpus import stopwords
import string

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
	cleared_question = [word[0] for word in question]
	cleared_question = ' '.join(cleared_question)
	print "Cleared:", cleared_question
	return cleared_question

	#tokenized_question = tokenize_question(question)
	#clearified_question = transformations.remove_stopwords(tokenized_question)
	
	#if question in knowledge_base:
	#	count = len(knowledge_base[question])
	#	return knowledge_base[question][random.randint(0,count-1)]
	#else:
	#	return get_sample_response()

def clear_question(question):
	for sym in punctuation:
		question = question.replace(sym,'')

	return question


def preprocess_question(question):
	"""sentences = nltk.sent_tokenize(question)"""
	lemmatizer = nltk.WordNetLemmatizer()
	
	sentences = nltk.word_tokenize(question) #for sent in question]
	sentences = [lemmatizer.lemmatize(word) for word in sentences]


	sentences = nltk.pos_tag(sentences) #for sent in sentences]

	
	print "Tagged"
	print sentences
	
	sentences = transformations.filter_insignificant(sentences)
	
	#sentences = transformations.swap_verb_phrase(sentences)
	print "after 1", sentences
	sentences = transformations.swap_infinitive_phrase(sentences)
	#print "after 2", sentences
	#sentences = transformations.singularize_plurar_noun(sentences)
	sentences = transformations.remove_stopwords(sentences)
	print "after 3", sentences
	#print "after 4", sentences

	#commands.execute(sentences)

	
	#print "NE:"
	#sent = sentences 
	#ne_sentences = nltk.ne_chunk(sent)
	#print ne_sentences
	
	return sentences #chunked

def regularize(tokens):
	"""Returns a copy of a regularized version of the token list.""" 
	tokenizer = nltk.tokenize.TreebankWordTokenizer()
	tokens = tokenizer.tokenize(tokens)
	#stemmer = nltk.PorterStemmer()

	stemmer = None
	STOPWORDS = [lemmatizer.lemmatize(t) for t in stopwords.words('english')]

	tokens = list(tokens)
	for i, token in enumerate(tokens):
        # Normalize text by case folding 
		token = token.lower()
		#print "token: ", token
        # Lemmatize (birds -> bird)
        token = lemmatizer.lemmatize(token)
        print "leman: ", token
        
        # Stopword and punctuation removal
        if token in STOPWORDS or token in string.punctuation:
        	token = None
        # Done; update value in list
        tokens[i] = token
    # Remove empty tokens 
	tokens = [x for x in tokens if x is not None]
	return tokens


def main():

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
    	print aiml_parser.respond(pattern)



if __name__ == "__main__":
    main()	