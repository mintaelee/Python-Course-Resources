class CallCount:
    def __init__(self, m):
        self.m = m
        self.count = 0
        
        def __call__(self, *args, **kwargs):
            self.count += 1
            return self.m(*args, **kwargs)
        

@CallCount
def hello(a_name):
    print('Hello, {}'.format(a_name))