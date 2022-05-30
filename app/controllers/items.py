import traceback

from redis_om import NotFoundError

from errors import SERVICE_ERROR_NONE
from errors import SERVICE_ERROR_NOT_FOUND
from errors import SERVICE_ERROR_SERVER_ERROR

from models.item import ITEM_STATUS_TODO
from models.item import Item

def items_get_all ():
	items = Item.find ().all ()
	print (items)
	return items

def item_create (data: dict):
	item = Item (
		task=data["description"],
		status=ITEM_STATUS_TODO
	)

	item.save ()
	item_id = item.pk
	print (item_id)

	return item_id

def item_update (item_pk: str, data: dict):
	error = SERVICE_ERROR_NONE

	try:
		item = Item.get (item_pk)

		item.task = data["description"]
		item.save ()

	except NotFoundError:
		print ("Failed to get item!")
		error = SERVICE_ERROR_NOT_FOUND
	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error

def item_change_status (item_pk: str, data: dict):
	error = SERVICE_ERROR_NONE

	try:
		item = Item.get (item_pk)

		item.status = data["status"]
		item.save ()

	except NotFoundError:
		print ("Failed to get item!")
		error = SERVICE_ERROR_NOT_FOUND
	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error

def item_remove (item_pk: str):
	error = SERVICE_ERROR_NONE

	try:
		Item.delete (item_pk)

	except NotFoundError:
		print ("Failed to get item!")
		error = SERVICE_ERROR_NOT_FOUND
	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error
