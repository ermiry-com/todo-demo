from redis import Redis
from redis_om import Migrator, JsonModel, Field

ITEM_STATUS_NONE = 0
ITEM_STATUS_TODO = 1
ITEM_STATUS_PROGRESS = 2
ITEM_STATUS_COMPLETE = 3

class Item (JsonModel):
	task: str = Field (index=False)
	status: int = Field (index=False)

	class Meta:
		database = Redis (host="cache", port=6379)

Migrator ().run ()
