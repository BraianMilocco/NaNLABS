import os
from fastapi import APIRouter, Request

from helpers.json_validation import validator
from helpers.json_validation import post_type
from helpers.task import create_task

router = APIRouter(
    # prefix="/app",
    tags=[],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_root():
    return {"Hello": os.getenv('trelloKey', None)}

@router.post("/")
async def read_root(request: Request):
    body = await request.json()
    type_ = post_type(body )
    validation_function = validator.get(type_)
    if not validation_function:
        return  {"Hello": 'error'}
    if not validation_function(body):
        return {"Hello": 'pero boludo'}
    
    return create_task(body)
    # return {"Hello": type_}