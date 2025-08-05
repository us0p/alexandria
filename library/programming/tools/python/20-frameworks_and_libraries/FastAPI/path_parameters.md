# Path parameters
You can declare path parameters or variables with the same syntax used by Python format strings:

You can declare the type of a path parameter in the function, using standard Python type annotations. With that type declaration, you receive automatic request "parsing", data validation and docs.
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
	return {"item_id": item_id} # will be an int
```

For Boolean parsing, you can receive any of the following values or any other case variation, in your API request:
- 1
- true
- on
- yes
# Path operation order
Because those operations are evaluated in order, you need to make sure that a **fixed path** is declared **before a dynamic path**.

It's also not possible to redefine a path operation. The first one will always be used since the path matches first.
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
	return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
	return {"user_id": user_id}
```
# Predefined values
If you want a path parameter to be predefined you can use Python `Enum`.
```python
from enum import Enum

from fastapi import FastAPI


# Inherit from 'str' so API docs will be able to know the type of the values.
class ModelName(str, Enum):
	alexnet = "alexnet"
	resnet = "resnet"
	lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
	if model_name is ModelName.alexnet:
		return {
			"model_name": model_name, # Converted to its corresponding value.
			"message": "Deep Learning FTW!"
		}

	# ...
```