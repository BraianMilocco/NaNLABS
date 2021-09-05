# from typing import Optional

from fastapi import FastAPI

from routers import api


app = FastAPI()

## Routes
app.include_router(api.router)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}