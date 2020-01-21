def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(args, **kwargs)
        return
    
    return wrap

class Trace:
    def __init__(self):
        self.enabled = True
    
    def __call__(self, m):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(m))
            return m(*args, **kwargs)
        return wrap
    
tracer = tracer()

@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + 'øy'


# Class Methods

class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix
        
    @tracer
    def make_island(self, name):
        return name + self.suffix
    