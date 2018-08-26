def decorate(func):
    cache = {}

    def wrap(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrap


@decorate
def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

print([fib(n) for n in range(10)])


# def fib2(n, cache=None):
#     if cache is None:
#         cache = {}
#     if n in cache:
#         return cache[n]
#     if n == 1 or n == 0:
#         return 1
#     else:
#         cache[n] = fib2(n-2, cache) + fib2(n-1, cache)
#         print(cache[n])
#         return cache[n]

# print([fib2(n) for n in range(40)])


