from datetime import datetime, timedelta
from time import sleep


class Product:
    website_name = "digikala.ir"

    def __init__(self, product_name: str, price: str, off: str) -> None:
        self.product_name = product_name
        self.price = price
        self.off = off

    @classmethod
    def info(cls):
        print(f"website name:{cls.website_name}")

    def __str__(self):
        return self.product_name


class Comment:
    def __init__(self, product: "Product", name: str, description: str, like_count: int, dislike_count: int) -> None:
        self.product = product
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.like_count = like_count
        self.dislike_count = dislike_count

    def show(self):
        print(f"product: {self.product}\n"
              f"name: {self.name}\n"
              f"description: {self.description}\n"
              f"date: {self.date}\n"
              f"like: {self.like_count} and dislike: {self.dislike_count}")

    @classmethod
    def censored(cls, comment: "Comment"):
        print("comment censored")
        comment.description = comment.description.replace("bishur", "*****")
        return comment

    @staticmethod
    def elapsed_time(time):
        sleep(10)
        print(datetime.now() - time)


Product.info()
c1 = Comment(Product("backpack", 0, 0), "bag", "khili bishur hasti", 23, 10)
c1.show()
print("*" * 40)
Comment.censored(c1)
c1.show()
print("*" * 40)
Comment.elapsed_time(c1.date - timedelta(days=5, hours=3))
