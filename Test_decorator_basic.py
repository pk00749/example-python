def meg(word='hello'):
    return word.upper()+'!'

print(meg())

my_meg = meg
print(my_meg)  # print cache address
print(my_meg())


def my_new_decorator(a_func_to_decorate):
    def the_wrapper_around_the_original_func():
        print("Before the func run")
        a_func_to_decorate()  # () is needed because run the decorated func
        print("After the func run")
    return the_wrapper_around_the_original_func


def a_stand_alone_func():
    print("I'm stand alone func, don't you dare modify me")

a_stand_alone_func()

# no () when it work as parameter to decorator and was passed to decorator
a_stand_alone_func_decorated = my_new_decorator(a_stand_alone_func)
a_stand_alone_func_decorated()

@my_new_decorator
def another_stand_alone_func():
    print("Leave me alone")

another_stand_alone_func()
