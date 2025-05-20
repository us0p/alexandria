# Query parameters and String Validations
In the example bellow, `q` is optional and its length can't exceed 50 characters.

```python
# Used to add metadata to your types
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items"):
async def read_items(
	q: Annotated[
		str | None,
		Query(max_length=50)
	] = None
):
	results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		results.update({"q": q})
	return results
```

This validation is also documented in the OpenAPI docs.

Using `Annotated` is recommended. The default value of the function parameter is the actual default value.

You could call that same function in other places without FastAPI, and it would work as expected.
## Query parameters multiple values
When you define a query parameter **explicitly with `Query`** you can also declare it to receive a list of values.
```python
from typing import Annotated

from fastapi import FastAPI, Query


app = FastAPI


@app.get("/items")
async def read_items(q: Annotated[list[str], Query()]):
	query_items = {"q": q}
	return query_items
```
## Declare more metadata
You can add more information about the parameter. That information will be included in the generated OpenAPI.
```python
# ...
async def read_items(
	q: Annotated[
		str | None,
		Query(
			title="Query string",
			description="Query string for the items to search the database",
			deprecated=True,
			include_in_schema=False, # Removes from OpenAPI docs.
			min_length=3,
		),
	]=None,
):
	# ...
```
## Alias parameters
If you need your parameter to have an invalid Python variable name, you can declare an `alias`, and that alias is what will be used to find the parameter value:
```python
# ...
async def read_items(
	q: Annotated[
		str | None,
		Query(alias="item-query")
	]=None
):
	# ...
```
## Custom Validation
You can use custom validator function that is applied after the normal validation.

You can achieve that using Pydantic's validator classes inside `Annotated`.
```python
from typing import Annotated

from pydantic import AfterValidator

# ...

def check_valid_id(id: str):
	# ...

# ...

async def read_items(
	id: Annotated[
		str | None,
		AfterValidator(check_valid_id)
	]=None,
):
	# ...
```

>These custom validators are for things that can be checked with only the same data provided in the request.
## Query parameters with a Pydantic model
Using a Pydantic model to represent a group of related query parameters allows for code reuse and encapsulation.
```python
from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
	limit: int = Field(100, gt=0, le=100)
	offset: int = Filed(0, ge=0)
	order_by: Literal["created_at", "updated_at"] = "created_at"
	tags: list[str] = []

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
	return filter_query
```

FastAPI will extract the data for each field from the query parameters in the request and give you the Pydantic model you defined.