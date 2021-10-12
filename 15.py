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
	},
	{
		"question": "The name Starbucks was inspired by which novel?",
		"answer": "Moby Dick"
	},
	{
		"question": "Who is the mother of North and Saint?",
		"answer": "Kim Kardashian"
	}

]

count = 0
for t in trivia_quiz:
    send_message(t["question"])
    response = read_message()
    if response == t["answer"]:
        send_message("Good Job!")
        count += 1
    else:
        send_message("Wrong! The correct answer is %s" % 
                      t["answer"])
      
send_message("You got %d answers correct!" % count)

if count < 2:
    send_message("Ouch!")
# Add elif and else
elif count < 4:
    send_message("Not bad...")
else:
    send_message("You rock!")


