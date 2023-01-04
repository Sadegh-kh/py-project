class User:
    def __init__(self, name: str, phone: str = " --- ") -> None:
        self.__user_id = id(self)
        self.name = name
        self.__phone = phone
        self.x = "+" + str(self.__user_id)

    def set_phone(self, phone: str) -> None:
        if len(phone) == 11 and phone.isdigit():
            self.__phone = phone

    def get_phone(self):
        return self.__phone.strip("0")


