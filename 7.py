welcome = "Hi! Let's put your trivia knowledge to the test. " \
          "I bet you will ace it!"
send_message(welcome)
trivia = {
		    "question": "Which city do the the Simpsons live in?",
		    "answer": "Springfield"
	     }
send_message(trivia["question"])

response = read_message()

if response.lower() == trivia["answer"].lower():
    send_message("Good Job!")
# Add else here
else:
    # Chatbot says "Wrong!"
    send_message("Wrong!")