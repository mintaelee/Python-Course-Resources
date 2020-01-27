# Example of a base class from The Python Journeyman book
# Chapter 8 p. 253

class Base:
    def __init__(self):
        print('Base initializer')
        
    def f(self):
        print('Base.f()')


# class Sub(Base):
#     pass

# class Sub(Base):
#     def f(self):
#         print('Sub.f()')

# Subclass initializers

class Sub(Base):
    def __init__(self):
        print('Sub initializer')
        
    def f(self):
        print('Sub.f()')