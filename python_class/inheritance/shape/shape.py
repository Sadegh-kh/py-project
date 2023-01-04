class Shape:
    def __init__(self, **kwargs):
        self.area = 0
        self.perimeter = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def show(self):
        info = ""
        for key, value in self.__dict__.items():
            if value > 0:
                info += f"{key} : {value}\n"
        print(info)

    def __str__(self):
        return self.__class__.__name__


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length=length, width=width)

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)


class Square(Shape):
    def __init__(self, length):
        super().__init__(length=length)

    def calculate_area(self):
        self.area = self.length ** 2

    def calculate_perimeter(self):
        self.perimeter = 4 * self.length


class Triangle(Shape):
    def __init__(self, base, height, side1, side2):
        super().__init__(base=base, height=height, side1=side1, side2=side2)

    def calculate_area(self):
        self.area = (self.base * self.height) / 2

    def calculate_perimeter(self):
        self.perimeter = self.base + self.side1 + self.side2



r = Rectangle(3.2, 4.3)
print("*" * 20, r, 20 * "*")
r.calculate_area()
r.calculate_perimeter()
r.show()
