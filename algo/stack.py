class Stack:
    def __init__(self, *args) -> None:
        self.objs = []
        for value in args:
            self.push(value)

    def push(self, obj) -> None:
        self.objs.append(obj)

    def pop(self) -> any:
        obj = self.objs[-1]
        self.objs.remove(obj)
        return obj

    def __str__(self) -> str:
        return str(self.objs)


if __name__ == "__main__":
    stack = Stack(1, 2, 3, 4)
    stack.pop()
    num = stack.pop()
    stack.push("ali")
    print(f"stack: {stack} ,pushed obj : 'ali' ,poped obj : {num}")
