# Enclosing Functions!

def enclosing():
    def locan_funct():
        print('locan function')
    return locan_funct 


# Play with this script to understand enclosing functions

######################
# Closure in Functions

def enclosing():
    my_str = 'close over'
    def locak_funct():
        print(my_str)
    return local_funct

# in terminal 
# >>> lf = enclosing
# >>> lf()
# Notice the message
# >>>lf.__closure__
# Notice the message


# Play with this script to understand Closures