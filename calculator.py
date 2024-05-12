def add(x, y):
    return x + y

def mul(x, y):
    return x*y

def sub(x, y):
    return x - y

def div(x, y):
    try:
        res = x/y
    except ZeroDivisionError as e:
        return e
    return res 
