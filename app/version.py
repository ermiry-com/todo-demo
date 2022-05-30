TODO_VERSION = "0.1"
TODO_VERSION_NAME = "Version 0.1"
TODO_VERSION_DATE = "29/05/2022"
TODO_VERSION_TIME = "19:25 CST"
TODO_VERSION_AUTHOR = "Erick Salas"

def todo_version_print_full ():
	print ("\nTodo Flask API Version: ", TODO_VERSION_NAME)
	print (
		"Release Date & time: ", TODO_VERSION_DATE, " - ", TODO_VERSION_TIME
	)

	print ("Author: ", TODO_VERSION_AUTHOR, "\n")

def todo_version_print_version_id ():
	print (
		"\nTodo Flask API Version ID: ", TODO_VERSION, "\n"
	)

def todo_version_print_version_name ():
	print (
		"\nTodo Flask API Version: ", TODO_VERSION_NAME, "\n"
	)
