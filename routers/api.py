import os
from fastapi import APIRouter, Request

from helpers.json_validation import validator
from helpers.json_validation import post_type

from helpers.messages import error_message
from helpers.apiGeneral import functions_card


router = APIRouter(
    tags=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_root():
    return error_message

@router.post("/")
async def read_root(request: Request):

    body = await request.json()
    type_ = post_type(body )
    validation_function = validator.get(type_)
    if not validation_function:
        return  error_message
    if not validation_function(body):
        return error_message

    return functions_card[type_](body)  
