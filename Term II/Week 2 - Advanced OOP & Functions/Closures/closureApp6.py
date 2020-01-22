# let's store the function name and the number of calls in a global dictionary instead of just printing it out all the time.

counters = dict()

def counter2(fn):
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is global
        return fn(*args, **kwargs)
    
    return inner

