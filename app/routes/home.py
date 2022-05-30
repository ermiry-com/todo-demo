from flask import Blueprint, render_template

from controllers.items import items_get_all

home = Blueprint ("home", __name__)

# GET /
@home.route ("/", methods=["GET"])
def homepage ():
	# fetch todo items from redis
	items, data = items_get_all ()

	# render home template with items table
	return render_template ("index.html", items=items, values=data)
