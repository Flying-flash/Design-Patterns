def decorator_function(original_function):
    def wrapper_function():
        return original_function
    print(original_function.__name__)
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display) #decorate_display is also called as decorated variable

decorated_display()

