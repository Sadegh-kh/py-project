from pprint import pprint


class BaceClass:
    num_base_calls = 0

    def __init__(self, a, b, **kwargs):
        self.a = a
        self.b = b

    def call_me(self):
        print("Calling method on BaseClass!")
        self.num_base_calls += 1
        # self.num_base_calls= self.num_base_calls + 1
        # self.num_base_calls = 0 + 1
        # self.num_base_calls = 1


class LeftSubClass(BaceClass):
    num_left_calls = 0

    def __init__(self, c, **kwargs):
        super().__init__(**kwargs)
        self.c = c

    def call_me(self):
        super().call_me()
        print("Calling method on LeftSubClass!")
        self.num_left_calls += 1


class RightSubClass(BaceClass):
    num_right_calls = 0

    def __init__(self, d, e, f, **kwargs):
        super().__init__(**kwargs)
        self.d = d
        self.e = e
        self.f = f

    def call_me(self):
        BaceClass.call_me(self)
        print("Calling method on RightSubClass!")
        self.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def __init__(self, g, **kwargs):
        super().__init__(**kwargs)
        self.g = g

    def call_me(self):
        BaceClass.call_me(self=self)
        print("Calling method on SubClass!")
        self.num_sub_calls += 1


obj = SubClass(a=1, b=2, c=3, d=4, f=5, e=6, g=7)
print(obj.a, obj.b, obj.c, obj.d, obj.f, obj.e, obj.g)
print()
print(
    f"obj.num_sub_calls: {obj.num_sub_calls}, obj.num_left_calls: {obj.num_left_calls}"
    f", obj.num_right_calls : {obj.num_right_calls},"
    f" obj.num_base_calls: {obj.num_base_calls} ")

pprint(SubClass.__mro__)
