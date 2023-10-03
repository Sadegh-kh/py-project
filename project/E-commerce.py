# products , shopping cart ,and user account
# methods adding and removeing from cart

import bcrypt
from typing import List


class Product:
    """product of my E-commerce"""

    def __init__(self, id_product: int, name: str, value: str) -> None:
        self.id_product = id_product
        self.name = name
        self.value = value

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class ShoppingCarts:
    """user's shoping carts for adding and removing products"""

    products: List[Product] = []

    def adding(self, product: Product) -> Product:
        """add product to shopping carts"""
        ShoppingCarts.products.append(product)
        return product

    def removeing(self, product: Product) -> None:
        """remove product from shopping carts"""
        ShoppingCarts.products.remove(product)


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class User(Person):
    def __init__(
        self, first_name: str, last_name: str, username: str, email: str, password: str
    ):
        super().__init__(first_name, last_name)
        self.username = username
        self.email = email
        self.__password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.__shopping_carts = ShoppingCarts()

    def adding_to_shopping_carts(self, product: Product):
        """add product to shopping carts"""
        self.__shopping_carts.adding(product)

    def remove_from_shopping_carts(self, product: Product):
        """remove product from shopping carts"""
        self.__shopping_carts.adding(product)

    def get_product_list(self) -> list:
        """it gives list of product"""
        return self.__shopping_carts.products


user = User("sadegh", "khoshbayan", "Sadegh", "Sadegh@gmail.com", "123")
product1 = Product(1, "laptop", "3500000")
product2 = Product(2, "keyboard", "200000")
user.adding_to_shopping_carts(product1)
user.adding_to_shopping_carts(product2)
print(user.get_product_list())
