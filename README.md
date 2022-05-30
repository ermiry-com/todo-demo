# Todo Demo

Ermiry TODO App Demo with Flask

### Development
```
sudo docker run \
  -it \
  --name todo --rm \
  -p 5000:5000 --net ermiry \
  -v /home/ermiry/Documents/projects/todo-demo:/home/todo \
  -e RUNTIME=development \
  -e PORT=5000 \
  ermiry/todo-demo:development /bin/bash
```

#### GET /api/todo
**Access:** Public \
**Description:** Todo demo service top level route \
**Returns:**
  - 200 on success

#### GET /api/todo/version
**Access:** Public \
**Description:** Returns todo demo service current version \
**Returns:**
  - 200 on success
