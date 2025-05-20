You can define Cookie parameters the same way you define `Query` and `Path` parameters.
```python
from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items")
async def read_items(ads_id: Annotated[str | None, Cookie()]=None):
	return {"ads_id": ads_id}
```
## Parameter Models
You can create a Pydantic model to declare a group of related cookies:
```python
from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
	session_id: str
	fatebook_tracker: str | None = None
	googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
	return cookies
```

> Browsers handle cookies in special ways an behind the scenes, they don't easily allow JavaScript to touch them. If you go to the API docs at `/docs` you'll be able to see the documentation for cookies for your path operations. But even if you fill the data and click "Execute", because the docs UI works with JavaScript, the cookies won't be sent, and you will see an error message.