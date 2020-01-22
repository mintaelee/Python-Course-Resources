'''
Instead of storing a list and reclaculating total and count every time wer need the new average, 
let's store the running total and count and update each value each time a new value is added to the running average, 
and then return total / count.

Let's start with a class approach first, where we will use instance variables to store the running total and count and provide an instance method to add a new number and return the current average.
'''

class Averager:
    def __init__(self):
        self._count = 0
        self._total = 0
    
    def add(self, value):
        self._total += value
        self._count += 1
        return self._total / self._count
    
# Now, let's see how we might use a closure to achieve the same thing.

def averager():
    total = 0
    count = 0
    
    def add(value):
        nonlocal total, count
        total += value
        count += 1
        return 0 if count == 0 else total / count
    
    return add