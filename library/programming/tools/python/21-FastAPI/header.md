```python
from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items")
async def read_items(user_agent: Annotated[str | None, Header()]=None):
	return {"User-Agent": user_agent}
```
## Automatic conversion
By default, `Header` will convert the parameter names characters from underscores to hyphen to extract and document the headers.

Also, HTTP headers are case-insensitive, so, you can declare them with standard snake case.