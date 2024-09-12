"""Base state for Twitter example. Schema is inspired by https://drawsql.app/templates/twitter."""
from typing import Dict, Optional

import reflex as rx
import requests
from twitter.db_model import User

class State(rx.State):
    """The base state for the app."""

    user: Optional[User] = None,
    # name: str = "name",
    # email: str = "example@email.com"
    # phone: str = "999999"
    products: list[str] = [{'Name'}]
    auth_token: str = rx.Cookie("auth_token", secure=True)

    def logout(self):
        """Log out a user."""
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            self.get_product_list()
            return rx.redirect("/login")
        
    def add_marketplace(self, form_data: dict):
        host = "http://localhost:8004"
        method = "/mp/add_ozon"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer "+self.auth_token,
            "Content-Type": "application/json"
        }

        data = {
            "mp_name": "ozon",
            "auth_data" : {
                "client_id": form_data['client_id'],
                "api_key": form_data['api_key']
            }
        }
        res = requests.post(host+method, json=data, headers=headers)
        print(res.status_code)


    def get_product_list(self):
        self.update_product_list()
        """returns product list"""
        host = "http://localhost:8004"
        method = "/products/all"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer "+self.auth_token,
        }
        res = requests.get(host+method, headers=headers)
        if res.status_code == 200 and res.json() != []:
            prodl = [[p["name"], 'ozon', p['price'], p['discount'], p['sku'] ]  for p in res.json()]
        else:
            prodl = [[
                "Name2", 
                "Email",
                "Age",
                # "Gender": "male",
                "Location",
                "Job",
                "Salary",
                "Actions",
            ]]
        print("get prod l", res.status_code)
        print(res.json())
        self.products = prodl
        return self.products

    def update_product_list(self):
        "make data reload from marketplace"
        host = "http://localhost:8004"
        method = "/products/update_list"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer "+self.auth_token,
        }
        res = requests.post(host+method, headers=headers)
        # print("res", res.text)
        # print("upd prod l", res.status_code)
            

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        if type(self.user) is type((1, 2)):
            return self.user[0] is not None
        return self.user is not None
        
        
