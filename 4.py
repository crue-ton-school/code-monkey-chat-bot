# Change the text of welcome:
welcome = "Hi! Let's put your trivia knowledge to the test. I bet you will ace it!" \


# Call the function send_message with the variable welcome
send_message(welcome)

send_message("What's your least favorite trivia topic?")
response = read_message()
send_message("I can barely answer questions on " + response)
