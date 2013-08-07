import nltk
import transformations

commands = ["open", "create", "find", "go", "remind"]

last_command_context = "NOT_SET"


def execute(chunk):
	verbs_in_chunk = get_all_pred_words(chunk, lambda (word, tag): tag.startswith('VB'))

	if not verbs_in_chunk:
		do_last_command_context_action(chunk)

	print "Verbs: ", verbs_in_chunk
	for verb in verbs_in_chunk:
		if verb[0] in commands:
			verb_id = get_word_index(verb, chunk)
			process_command(chunk, chunk[verb_id][0], verb_id)
			

def process_command(chunk, verb, start_searching_noun_id):
	noun_id = transformations.first_chunk_index(chunk, lambda (word, tag): tag.startswith('NN'), start = start_searching_noun_id, step = 1)
	execute_command(verb, chunk[noun_id][0])

def do_last_command_context_action(chunk):
	process_command(chunk, last_command_context, 0)
		

def execute_command(verb, noun):
	global last_command_context

	if verb == "open":
		print "I'm opening '", noun, "' for you! :)"
		last_command_context = "open"

	elif verb == "create":
		print "I'm create '", noun, "' for you! :)"
		last_command_context = "create"

	elif verb == "find":
		print "I'm looking for  '", noun, "' for you! :)"
		last_command_context = "find"

	elif verb == "go":
		print "I'm going to '", noun, "' for you! :)"
		last_command_context = "go"

	elif verb == "remind":
		print "I'm will remind you about '", noun, "'' for you! :)"
		last_command_context = "remind"
	else:
		print "Don't know what just happened x_X (", verb, noun, ")"
		last_command_context = "NOT_SET"
	 
	print "Last context set to: ", last_command_context


def get_all_pred_words(chunk, pred):
	verbs = []
	l = len(chunk)

	for i in range(0, l):
		if pred(chunk[i]):
			verbs.append(chunk[i])

	return verbs


def get_word_index(word, chunk):
	l = len(chunk)

	for i in range(0, l):
		if chunk[i] == word:
			return i

	return -1 #not found


def get_verb_from_chunked_sentence(chunk):
	vbdix = transformations.first_chunk_index(chunk, lambda (word, tag): tag.startswith('VB'))
	return vbdix
    
