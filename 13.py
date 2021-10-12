welcome = "Hi! Let's put your trivia knowledge to the test. " \
          "I bet you will ace it!"
send_message(welcome)
trivia_quiz = [
    {
		"question": "What is the name of Harry Potter's school?",
		"answer": "Hogwarts"
	},
	{
		"question": "Who was the first Disney Princess?",
		"answer": "Snow White"
	},
	{
		"question": "Who is Stefani Joanne Angelina Germanotta?",
		"answer": "Lady Gaga"
	}
]


for t in trivia_quiz:
    send_message(t["question"])
    # Read the user's response and store it
    response = read_message()
    if response == t["answer"]:
        send_message("Good Job!")
    else:
        send_message("Wrong! The correct answer is %s" % 
                      t["answer"])
        