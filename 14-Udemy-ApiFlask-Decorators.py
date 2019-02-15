#Decorators Examples
# Decorator without Parameters
import functools
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_fun():
        print("Tn the decorator")
        func()
        print ("After the Decorator")
    return function_that_runs_fun
@my_decorator
def my_function():
    print ("I'm the function")
my_function()

#Decorator with parameters

def decorator_with_argumments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs): #because function can pass own data
            print ("In the decorator!")
            if number == 56:
                print ("Not running the function")
            else:
                func(*args, **kwargs)
            print("After decorator!")
        return function_that_runs_func
    return my_decorator


@decorator_with_argumments (55)
def my_function_too(x, y):
    b=x+y
    print ("hello: {}".format(b))

my_function_too(57,67)
