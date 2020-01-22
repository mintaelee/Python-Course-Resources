'''
we can essentially be able to convert a class to an equivalent functionality using closures. 
This is actually true in a much more general sense - very often, classes that define a single method (other than initializers) can be implemented using a closure instead.

Let's look at another example of this.

Suppose we want something that can keep track of the running elapsed time in seconds.
'''

from time import perf_counter
class Timer:
    def __init__(self):
        self._start = perf_counter()
    
    def __call__(self):
        return (perf_counter() - self._start)
    
# Now let's rewrite this using a closure instead:

def timer():
    start = perf_counter()
    
    def elapsed():
        # we don't even need to make start nonlocal 
        # since we are only reading it
        return perf_counter() - start
    
    return elapsed

