def memoize(fun):
    memory = {}

    def start(*args, **kwargs):
        if args not in memory:
            memory[args] = fun(*args)
        return memory[args]

    return start


@memoize
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(40))
