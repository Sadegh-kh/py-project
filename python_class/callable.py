class A:
    def __init__(self, x):
        print("init")
        self.x = x

    def __call__(self, *args, **kwargs):
        print("call")
        self.x = args


a = A(2)
print(a.x)
a(3, 4)
print(a.x)
