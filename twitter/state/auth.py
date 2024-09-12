"""The authentication state."""
from asyncio import sleep
import reflex as rx
from sqlmodel import select

import requests

from .base import State, User


class AuthState(State):
    """The authentication state for sign up and login page."""

    username: str
    password: str
    confirm_password: str

    def signup(self):
        """Sign up a user."""
        if self.password != self.confirm_password:
            return rx.window_alert("Passwords do not match.")
        
        db_url = "http://localhost:8004" # need change later!

        method = "/users"
        headres = {
            'Content-Type': 'application/json',
        }
        data = {
            "email": self.username,
            "password_hash": self.password
        }

        response = requests.post(db_url+method, json=data, headers=headres)
        if response.status_code != 200:
            return rx.window_alert("Username already exists.")
        
        self.user = User(username=self.username, password=self.password)
        
   
        method = "/token"
        headres = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        json =  {
            "username": self.username,
            "password": self.password
        }
 
        response = requests.post(db_url+method, data=json, headers=headres)
        tkn = response.json()['access_token']
        self.auth_token = tkn
        
        # uuid = response.json()

        # self.token = uuid["access_token"]

        # if session.exec(select(User).where(User.username == self.username)).first():
        #     return rx.window_alert("Username already exists.")
        # self.user = User(username=self.username, password=self.password)
        return rx.redirect("/")
        
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords do not match.")
            if session.exec(select(User).where(User.username == self.username)).first():
                return rx.window_alert("Username already exists.")
            self.user = User(username=self.username, password=self.password)
            # session.add(self.user)
            # session.expire_on_commit = False
            session.commit()
            return rx.redirect("/")

    def login(self):
        """Log in a user."""
        db_url = "http://localhost:8004" # need change later!
        method = "/token"
        headres = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        json =  {
            "username": self.username,
            "password": self.password
        }

        response = requests.post(db_url+method, data=json, headers=headres)
        
        if response.status_code != 200:
            return rx.window_alert("No such user")
        
        self.user = User(username=self.username, password=self.password)
        self.auth_token = response.json()["access_token"]
        # print('auth', self.auth_token)

        return rx.redirect("/")
    
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.username == self.username)
            ).first()
            if user and user.password == self.password:
                self.user = user
                return rx.redirect("/")
            else:
                return rx.window_alert("Invalid username or password.")
