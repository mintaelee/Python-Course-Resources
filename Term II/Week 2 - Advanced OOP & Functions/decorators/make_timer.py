import time
     
def make_timer():
    last_called = None
        
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            las_called = now
            return None
        result = now - last_called
        last_called = now
        return result
            
    return elapsed

# in the terminal
# >>> from make_timer import make_timer
# >>> tm = make_timer()
# >>> tm()
# >>> tm()
# >>> tm()

# Notice that the frist time we call this function nothing happens but everytime after that, 
# it invokes the last time the function was called!

# How does this work: well every time the function is called, a new local variable is created naned 'last_call',
# then, a new function defined last is created which uses a new nonlocal key binding and inserting the function last_called into its local scope.
# The last_called then uses the new key binding to keep tract of the last time it was called.
# Play with this script to understand local and nonlocal bindings.
# Take Notice that when running this script in the terminal that creating new different objects of the function
# will define new and unrelated function calls between the obejcts.  in other words, new objects created will have no effect 
# on the previews objects already defined!