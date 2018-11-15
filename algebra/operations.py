

def sum(*args):
    """
    This function returns the sum of two number.
    """
    
    tot = 0
    for num in args:
       tot += num

    return tot


def product (*args):
    """
    This function return the product of two number
    """
    
    tot = 1
    for num in args:
        tot *= num

    return tot
