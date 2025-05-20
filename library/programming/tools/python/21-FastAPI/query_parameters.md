# Query parameters
When you declare other function parameters that are not part of the parameters, they are automatically interpreted as "query" parameters.
```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
	{"item_name": "Foo"},
	{"item_name": "Bar"},
	{"item_name": "Baz"}
]

@app.get("/items"):
async def read_items(skip: int = 0, limit: int = 10):
	return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}"):
# Optional query parameter uses default value 'None'.
async def read_item(item_id: int, q: str | None = None):
	if q:
		return {"item_id": item_id, "q": q}
	return {"item_id": item_id}
```

>Having a default value of any type, including `None`, makes the parameter optional (not required).

## Required, can be `None`
You can declare that a parameter can accept `None`, but that it's still required. Clients would need to send a value, even if the value is `None`.

To do that, you can declare that `None` is a valid type but simply do not declare a default value.