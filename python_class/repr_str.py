class Person:
    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.firstname}' , '{self.lastname}' , {self.age})"


hasnali = Person("hasnaali", "kargar", 20)
print(str(hasnali))
print(repr(hasnali))

