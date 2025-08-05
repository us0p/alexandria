# Path Parameter
Work the same as [Query](query_parameter_and_string_validations.md), you can declare the same type of validations and metadata for path parameters with `Path`.
```python
from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/item/{item_id}")
async def read_items(
	item_id: Annotated[
		int,
		Path(
			title="The ID of the item to get",
			ge=1, # greater or equal
			le=5  # less or equal
		)
	],
	size: Annotated[
		float,
		Query(
			gt=0,   # greater than
			lt=10.5 # less than
		)
	],
	q: Annotated[str | None, Query(alias="item-query")] = None,
):
	results = {"item_id": item_id}
	if q:
		results.update({"q": q})
	return results
```