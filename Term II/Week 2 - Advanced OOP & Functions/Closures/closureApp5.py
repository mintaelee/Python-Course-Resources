# now build something that can run, and maintain a count of how many times we have run some function.

def counter(fn):
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    
    return inner

def add(a, b):
    return a + b
