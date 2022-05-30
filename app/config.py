import os

from runtime import runtime_from_string, runtime_to_string

RUNTIME = runtime_from_string (os.environ.get ("RUNTIME"))

PORT = int (os.environ.get ("PORT"))

TIME_SERVICE_ADDRESS = os.environ.get ("TIME_SERVICE_ADDRESS")

def todo_config ():
	print ("RUNTIME: ", runtime_to_string (RUNTIME))

	print ("PORT: ", PORT)

	print ("TIME_SERVICE_ADDRESS: ", TIME_SERVICE_ADDRESS)
