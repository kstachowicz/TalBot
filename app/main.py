import random

sample_responses = ["mhm", "and then what..?", "that's interesting", "tell me more :)"]

knowledge_base = {"WHO ARE YOU": ["I am Tala. And I'm a bot.", "And you?", "Not you business."],
				"WWW": ["I'm from Poland", "From home", "From internet ;)"],
				"HOW OLD ARE YOU": ["100", "200", "300"]}

punctuation = '.?!'

def get_sample_response():
	count = len(sample_responses)
	return sample_responses[random.randint(0,count-1)]

def get_answer(question):
	if question in knowledge_base:
		count = len(knowledge_base[question])
		return knowledge_base[question][random.randint(0,count-1)]
	else:
		return get_sample_response()

def clear_question(question):
	for sym in punctuation:
		question = question.replace(sym,'')

	return question


def process_question(question):
	question = question.upper()
	clearified_question = clear_question(question)
	
	return clearified_question

def main():
	question = ""
	previous_question = ""
	print "Hi, How can I help you?"
	while question != "0":
		question = raw_input()
		question = process_question(question)
		if previous_question == question:
			print "I've just told you!"
			continue;

		previous_question = question	
		answer = get_answer(question)
		print answer


if __name__ == "__main__":
	main()	