x = [1]
print(id(x))
print(id(x))
def func():
    x.append(2)
    print(id(x))

func()
print(x)