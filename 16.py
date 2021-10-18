# Define welcome text
welcome = "Hello! My name is Dawid, and I'm a Trivia chatbot!"
send_message(welcome)

# Define question and answer
# Add more questions to make your chatbot more fun!
trivia_quiz = [
    {
		"question": "What is the oldest country's name?",
		"answer": "San Marino",
	    	"really": "America"
	}
]

count = 0
for t in trivia_quiz:
    send_message(t["question"])
    response = read_message()
    if response == t["answer"]:
        # Define text when the user answer correctly
        send_message("Good Job!")
        count += 1
    if response == t["really"]:
	send_message("You can't honestly be this stupid?")
    else:
        # Define text when the user didn't answer correctly
        send_message("%s is actually correct!" % 
                      t["answer"])
 
 # Define text with the number of correct answer     
send_message("You got %d answers correct!" % count)

# Define text at the end of chat based on how many
# correct answers user got
if count < 2:
    send_message("Try better next time!")
elif count < 4:
    send_message("Not bad...")
else:
    send_message("Amazing Job!")


