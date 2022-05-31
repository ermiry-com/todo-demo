from flask import Blueprint, request, jsonify

from errors import response_from_error

from controllers.items import item_create
from controllers.items import item_update
from controllers.items import item_change_status
from controllers.items import item_remove

items = Blueprint ("items", __name__)

# POST /api/todo/items/create
@items.route ("/api/todo/items/create", methods=["POST"])
def item_create_handler ():
	data = request.get_json ()
	error, item_id = item_create (data)
	return jsonify ({"oki": "doki"})

# PUT /api/todo/items/:item_id/update
@items.route ("/api/todo/items/<item_id>/update", methods=["PUT"])
def item_update_handler (item_id):
	data = request.get_json ()
	error = item_update (item_id, data)

	return jsonify (response_from_error (error)), error

# PUT /api/todo/items/:item_id/status
@items.route ("/api/todo/items/<item_id>/status", methods=["PUT"])
def item_status_handler (item_id):
	data = request.get_json ()
	error = item_change_status (item_id, data)

	return jsonify (response_from_error (error)), error

# DELETE /api/todo/items/:item_id/remove
@items.route ("/api/todo/items/<item_id>/remove", methods=["DELETE"])
def item_remove_handler (item_id):
	error = item_remove (item_id)

	return jsonify (response_from_error (error)), error
