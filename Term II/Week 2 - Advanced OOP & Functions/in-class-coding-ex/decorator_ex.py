def decoratorFunc(args):
    # Code to you want to execute
    ...

@decoratorFunc
def existingFunction(args):
    # Code that you want to decorate
    


def top(func):
    def wrapper(*args, **kwargs):
        print("1" * 1)
        func(*args, **kwargs)
        print("1" * 1)
    return wrapper

def middle(func):
    def wrapper(*args, **kwargs):
        print("2" * 2)
        func(*args, **kwargs)
        print("2" * 2)
    return wrapper

def bottom(func):
    def wrapper(*args, **kwargs):
        print("3" * 3)
        func(*args, **kwargs)
        print("3" * 3)
    return wrapper

@top
@middle
@bottom
def myTest(anyString):
    print(anyString)

myTest("Hello World!")


def decorate(func):
       def first():
      func()
      print("This is the First Program on Decorators.")
   return first

def hello_not_decorated():
   print("Hello World!.\n")

print("This is an original function that is not decorated : ")

hello_not_decorated()
print("This is a decorated function :")
@decorate
def hello():
   print("Hello World!.")

hello()

#1 Output:

# This is an original function that is not decorated : 
# Hello World!.

# This is a decorated function :
# Hello World!.
# This is the First Program on Decorators.

