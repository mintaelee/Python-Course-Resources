# Recall the simple closure to count how many times a function had been run:

def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

# Now, 

def add(a, b=0):
    """
    returns the sum of a and b
    """
    return a + b

# call that counter function a decorator.
# There is a shorthand way of decorating our function without having to type: 
# func = counter(func)

@counter
def mult(a: float, b: float=1, c: float=1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c

