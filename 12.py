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
	    
	    # Add another "question" & "answer"
	    "question": "Who is Stefani Joanne Angelina Germanotta?",
	    "answer": "Lady Gaga"
	    
	}
]

# Use a for to send all questions
for t in trivia_quiz:
    send_message(t["question"])