#!/usr/bin/python3
"""
module inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class has public attributes
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Review constructor"""
        super().__init__(*args, **kwargs)
