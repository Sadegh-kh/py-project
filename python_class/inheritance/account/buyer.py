from users import User


class Buyer(User):
    def __init__(self, user_name: str, email: str, password: str, phone: str) -> None:
        super().__init__(user_name, email, password)
        super().all_users.append(self)
        self.phone = phone





def main():
    buye_1 = Buyer("karimi","karim@gmail.com","3223sdfsa","322345688")
    print(buye_1)


if __name__ == "__main__":
    main()
