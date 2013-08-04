import random

sample_responses = ["mhm", "and then what..?", "that's interesting", "tell me more :)"]

knowledge_base = {"who are you?": ["I am Tala. And I'm a bot.", "And you?", "Not you business."],
				"www": ["I'm from Poland", "From home", "From internet ;)"],
				"how old are you?": ["100", "200", "300"]}

def get_sample_response():
	count = len(sample_responses)
	return sample_responses[random.randint(0,count-1)]

def get_answer(question):
	if question in knowledge_base:
		count = len(knowledge_base[question])
		return knowledge_base[question][random.randint(0,count-1)]
	else:
		return get_sample_response()

def main():
	question = ""
	print "Hi, How can I help you?"
	while question != "0":
		question = raw_input()
		answer = get_answer(question)
		print answer


if __name__ == "__main__":
	main()	