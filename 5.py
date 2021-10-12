welcome = "Hi! Let's put your trivia knowledge to the test. " \
          "I bet you will ace it!"

send_message(welcome)

trivia = {
		   "question": "Which game is played in the Super Bowl?",
		   "answer": "football"
	}


# Send trivia question
send_message(trivia["question"])
# Send trivia answer
send_message(trivia["answer"])