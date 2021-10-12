welcome = "Hi! Let's put your trivia knowledge to the test. " \
          "I bet you will ace it!"
send_message(welcome)
trivia = {
		    "question": "Which city do the the Simpsons live in?",
		    "answer": "Springfield"
	     }
send_message(trivia["question"])

response = read_message()

# Use if to check if response equals the answer
if response == trivia["answer"]:
    # Chatbot says "Good job!"
    send_message("Good job!")