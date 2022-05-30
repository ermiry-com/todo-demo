from flask import Blueprint, jsonify

import version

service = Blueprint ("service", __name__)

# GET /api/todo
@service.route ("/api/todo", methods=["GET"])
def todo_handler ():
	return jsonify ({"msg": "Todo works!"}), 200

# GET /api/todo/version
@service.route ("/api/todo/version", methods=["GET"])
def todo_version_handler ():
	v = f"{version.TODO_VERSION_NAME} - {version.TODO_VERSION_DATE}"
	return jsonify ({"version": v}), 200
