import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def logger_func(*args):
        logging.info('Running"{}" with arguments {}'.format(func.__name__,args))
        print(func(*args))
    return logger_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

h1= logger(add)
h1(3,5)
print(h1.__name__)
print(add.__name__)
print(logger.__name__)