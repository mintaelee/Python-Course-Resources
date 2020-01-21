class Trace:
    def __init__(self):
        self.enabled = True
    
    def __call__(self, m):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(m))
            return m(*args, **kwargs)
        return wrap
    
tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]



        