from functools import lru_cache

@lru_cache(maxsize = None)
def fib(n):
    if n <=0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# print(fib(300))
def fib_gen():
    f1 = 1
    f2 = 1
    while True:
        f1, f2 = f2, f1 + f2
        yield f2

gen = fib_gen()
# for i in range(10):
    # print(next(gen))


class FibClass:
    def __init__(self, n):
        self.now = FibClass.fib_start(self, n)
        self.old = FibClass.fib_start(self, n-1)

    @lru_cache(maxsize = None)
    def fib_start(self, n):
        if n <=0:
            return 1
        else:
            return FibClass.fib_start(self, n-1) + FibClass.fib_start(self, n-2)

    def get(self):
        return self.now

    def next(self):
        self.old, self.now = self.now, self.now + self.old



f = FibClass(100)
print(f.get())
f.next()
print(f.get())
