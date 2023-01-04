from users import User
from pprint import pprint


class Seller(User):
    def order(self, order: "Order"):
        print(f"{self.user_name} , your product , {order} has been sold ")



def main():
    ali = Seller("ali", "aliabas@gmail.com", "3223234313")
    sadegh = User("sadegh", "sadegherwf@gmail.com", "3224dsf1532")
    ali.order("Compound effect")
    Seller.all_users = []
    pprint(Seller.all_users)
    pprint(User.all_users)


if __name__ == "__main__":
    main()
