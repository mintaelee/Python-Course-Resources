g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    inner()


# play with this script to better understand the logic of the LEGB rule
# LEGB - Locan, Enclosing, Global & Built-in