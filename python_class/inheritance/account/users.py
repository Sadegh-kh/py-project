from typing import List
from pprint import pprint


class UserList(list["User"]):
    def search(self, user_name: str) -> list["User"]:
        matching_users: list["User"] = []
        for user in self:
            if user_name in user.user_name:
                matching_users.append(user)
        return matching_users


class User:
    all_users: List["User"] = UserList()

    def __init__(self, user_name: str, email: str, password: str) -> None:
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.user_name!r},{self.email!r},{self.password!r})"


def main():
    amin = User("amin", "aminKaabiri@gmail.com", "32241532")
    amin.all_users = []
    abas = User("abas", "assdf@gmail.com", "3224a331532")
    hydr = User("hydr", "hydr@gmail.com", "3224a331532")
    hossain = User("hossain", "hossainali@gmail.com", "3224a331532")
    pprint(amin.all_users)
    pprint(abas.all_users)
    print("*"*40)
    pprint(User.all_users.search("amin"))


if __name__ == "__main__":
    main()
