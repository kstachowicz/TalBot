import aiml

k = aiml.Kernel()
k.learn("brain.xml")
print "x"
k.respond("LOAD AIML B")
#k.learn("aiml sets/aiml/*")
print "after"
k.setBotPredicate("name", "Chatty")

while True:
	input = raw_input("> ")
	response = k.respond(input)

	print response

