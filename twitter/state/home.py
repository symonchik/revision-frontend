"""The state for the home page."""
from datetime import datetime

import reflex as rx
from sqlmodel import select

from .base import State
# from twitter.db_model import Follows, Tweet, User

class HomeState(State): 
    """The state for the home page."""

    
