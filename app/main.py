import random

sample_responses = []

def prepare_sample_responses():
	global sample_responses
	sample_responses = ["mhm", "and then what..?", "that's interesting", "tell me more :)"]
	"""print sample_responses[:]"""

def get_sample_response():
	count = len(sample_responses)
	return sample_responses[random.randint(0,count-1)]

def main():
	prepare_sample_responses()
	answer = ""
	print "Hi, How can I help you?"
	while answer != "0":
		answer = raw_input()
		response = get_sample_response()
		print response


if __name__ == "__main__":
	main()	