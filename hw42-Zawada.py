# This program will greet the user and wait for a greeting in return.
# It will then greet the user with a version of the user's greeting.
# This will continue forever.
# Update the code to exit (finish) once the user says:
#    "What's up?"
# Meanwhile, you can kill a process with Ctrl-C, or the red square in PyCharm

INITIAL_GREETING = "What's up?"
greeting = input(INITIAL_GREETING + "\n")
while greeting != "What's up?":
  print (greeting + "\n") 
  greeting = input(INITIAL_GREETING + "\n")
