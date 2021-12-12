from typing import List

from system.databases.product_db import AbstractAdminProductDB
from system.databases.user_db import AbstractAdminUserDB, UserDB
from system.models.shopping import Product
from system.models.users.abstract_user import AbstractUser
from system.models.users.customer import Customer
from system.models.users.user import User


class Admin(User, AbstractUser, AbstractAdminProductDB, AbstractAdminUserDB):
    def __init__(self, user_name: str, password: str):
        User.__init__(self, user_name, password, 1, -1)
        self.user_db = UserDB("system/databases/csv/user_db")

    def add_product(self, product: Product):
        self.product_db.add_product(product)

    def remove_product(self, product: Product):
        self.product_db.remove_product(product)

    def edit_product(self, product: Product, column: int, new_value: str):
        self.product_db.edit_product(product, column, new_value)

    def get_customer(self, user_name: str) -> Customer:
        return self.user_db.get_customer(user_name)

    def get_all_customers(self) -> List[Customer]:
        return self.user_db.get_all_customers()

    def set_customer_discount(self, user_name: str, discount_id: int):
        self.user_db.set_customer_discount(user_name, discount_id)
