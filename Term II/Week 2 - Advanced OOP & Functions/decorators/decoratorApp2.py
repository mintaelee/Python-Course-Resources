def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

@counter
def add(a: int, b: int=10) -> int:
    """
    returns sum of two integers
    """
    return a + b

