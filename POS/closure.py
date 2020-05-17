def outer_func():
    message='Hi'

    def inner_func():
        print(message)
    return inner_func

h1 = outer_func()
h1()
print(h1.__name__)