# Request Body
To declare a request body, you use Pydantic models.
```python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
	name: str,
	description: str | None = None # Not required
	price: float
	tax: float | None = None # Not required


app = FastAPI()


@app.post("/items"):
async def create_item(item: Item):
	return item
```

With this, FastAPI will:
- Read the body of the request as JSON.
- Convert the corresponding types.
- Validate the data.
- Generate JSON schema as part of the OpenAPI schema.

You can also declare body parameters as optional, by setting the default to `None`.
# Request body + path + query parameters
FastAPI will recognize that the function parameters that are declared to be Pydantic models should be taken from the request body.

The function parameter will be recognized as follows:
- Parameter is also declared in the path, it'll be used as a path parameter.
- Parameter is of a singular type (`int`, `float`, `str`, `bool`, etc) it will be interpreted as a query parameter.
- Parameter is declared to be of the type Pydantic model, it will be interpreted as a request body.

>Note that FastAPI detect parameters by their names, types and default declarations (`Query`, `Path`, etc), it doesn't care about the order.
## Multiple body parameters
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
	name: str
	description: str | None = None
	price: float
	tax: float | None = None


class User(BaseModel):
	username: str
	full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
	results = {"item_id": item_id, "item": item, "user": user}
	return results
```

Notice that there is more than one body parameter in the function. So it'll then use the parameter names as keys in the body, and expect a body like:
```python
{
	"item": {
		"name": "Foo",
		"description": "The pretender",
		"price": 42.0,
		"tax": 3.2
	},
	"user": {
		"username": "dave",
		"full_name": "Dave Grohl"
	}
}
```
## Singular values in body
The same way there is a [Query](query_parameter_and_string_validations.md) and [Path](path_parameter_and_numeric_validations.md) to define extra data for query and path parameters. FastAPI provides an equivalent `Body`.
```python
from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
	name: str
	description: str | None = None
	price: float
	tax: float | None = None


class user(BaseModel):
	username: str
	full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
	item_id: int,
	item: Item,
	user: User,
	importance: Annotated[int, Body()]
):
	results = {
		"item_id": item_id,
		"item": item,
		"user": user,
		"importance": importance
	}
	return results
```

In this case, FastAPI will expect a body like
```python
{
	"item": {
		"name": "Foo",
		"description": "The pretender",
		"price": 42.0,
		"tax": 3.2
	},
	"user": {
		"username": "dave",
		"full_name": "Dave Grohl"
	},
	"importance": 5
}
```

>`Body` also has all the same extra validation and metadata parameters as `Query`, `Path` and others you will see later.
## Embed a single body parameter
If you want to expect a JSON with a key `item` and inside of it the model contents:
```python
# ...

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
	results = {"item_id": item_id, "item": item}
	return results
```

In this case FastAPI will expect a body like
```python
{
	"item": {
		"name": "Foo",
		"description": "The pretender",
		"price": 42.0,
		"tax": 3.2
	}
}
```
## Body - Fields
You can declare validation and metadata inside of Pydantic models using Pydantic's `Fild`.
```python
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
	name: str
	description: str | None = Field(
		default=None,
		title="The description of the item",
		max_length=300
	),
	price: float = Field(
		gt=0,
		description="The price must be greater than zero"
	),
	tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
	results = {"item_id": item_id, "item": item}
	return results
```

`Field` works the same way as `Query`, `Path` and `Body`, it has all the same parameters, etc.

>Actually, `Query`, `Path` and others create objects of subclasses of a common `Param` class, which is itself a subclass of Pydantic's `FieldInfo` class.
>And Pydantic's `Field` returns an instance of `FieldInfo` as well.
>`Body` also returns objects of a subclass of `FieldInfo` directly. And there are others that are subclasses of the `Body` class.
## Bodies of pure lists
If the top level value of the JSON body you expect is a JSON `array`, you can declare the type in the parameter of the function, the same as in Pydantic models:
```python
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
	url: HttpUrl
	name: str


@app.post("/images/multiple")
async def create_multiple_images(images: list[Image]):
	return images
```
## Bodies of arbitrary `dict`
You can also declare a body as a `dict`. This way, you don't have to know beforehand what the valid field/attribute names are (as would be the case with Pydantic models).
```python
from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights")
async def create_index_weights(weights: dict[int, float]):
	return weights
```