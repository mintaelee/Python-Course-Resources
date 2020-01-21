def noop(x):
    def noop_wrapper():
        return x()
    
    noop_wrapper.__name__ = x.__name__
    noop_wrapper.__doc__ = x.__doc__
    return noop_wrapper

@noop
def hello():
    "Print a well-known quote."
    print('Hello, ladies!')
    
# Now with functools

# import functools

# def noop(x):
#     @functools.wraps(x)
#     def noop_wrapper():
#         return x()

# @noop
# def hello():
#     "Print a well-known quote."
#     print('Hello, ladies!')