from typing import List
from abc import ABC, abstractmethod
from system.models.users.customer import Customer
from system.models.shopping.order import Order
from system.models.shopping.product import Product
from system.models.shopping.country import Country


class AbstractProductDB(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def remove_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self, product: Product, column: int, new_value: str):
        pass

    @abstractmethod
    def sub_product_quantity(self, product: Product, amount: int):
        pass

    @abstractmethod
    def get_product(self, product_name: str):
        pass

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass

    @abstractmethod
    def product_exists(self, product_name: str) -> bool:
        pass


class AbstractUserDB(ABC):
    @abstractmethod
    def add_customer(self, customer: Customer):
        pass

    @abstractmethod
    def get_user(self, user_name: str):
        pass

    @abstractmethod
    def get_customer(self, user_name: str):
        pass

    @abstractmethod
    def get_all_customers(self) -> List[Customer]:
        pass

    @abstractmethod
    def set_customer_discount(self, user_name: str, discount_id: int):
        pass

    @abstractmethod
    def user_exists(self, user_name: str) -> bool:
        pass


class AbstractOrderDB(ABC):
    @abstractmethod
    def add_order(self, order: Order):
        pass

    @abstractmethod
    def update_order_subtotals(self, user_name: str, discount_percentage: float):
        pass

    @abstractmethod
    def get_customer_orders(self, user_name: str) -> List:
        pass

    @abstractmethod
    def orders_exist(self, user_name: str) -> bool:
        pass


class AbstractCountryDB(ABC):
    @abstractmethod
    def get_country(self, country_id: int):
        pass

    @abstractmethod
    def get_all_countries(self) -> List[Country]:
        pass
