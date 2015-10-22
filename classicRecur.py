# this module includes simplest recursive functions to start with


# recursive factorial
def FactR(num):
    """assumes that intger is an int > 0 returns the factorial num!"""
    if num == 1:
        return num
    return num * FactR(num-1)
