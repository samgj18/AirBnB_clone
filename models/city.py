#!/usr/bin/python3
"""
module inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""