# Let's build an averager function that can average multiple values.

class Averager:
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count
    
