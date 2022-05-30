from flask import Flask

from config import PORT, todo_config
from version import todo_version_print_full

from routes.home import home
from routes.items import items
from routes.service import service

app = Flask (__name__)

app.register_blueprint (home)
app.register_blueprint (items)
app.register_blueprint (service)

if __name__ == "__main__":
	todo_version_print_full ()

	todo_config ()

	app.run (debug=True, host="0.0.0.0", port=PORT)
