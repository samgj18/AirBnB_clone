#!/usr/bin/python3
"""
module inherits from BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    public class attrb name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """State constructor"""
        super().__init__(*args, **kwargs)
