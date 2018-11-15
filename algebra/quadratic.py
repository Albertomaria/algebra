

def poly (*args):
    """

    f(x)  = a*x + b * x**2 + c * x**3 + ...

    *args = (x,a,b)
    """
    if len(args) ==1:
        raise Exception ("You have only entered a value for x, and no coefficents.")

    x = args[0] # X value
    coef = args[1:]
    result = 0
    for power, c in enumerate(coef):
        result += c * (x ** power + 1)

    return result
