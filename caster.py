def getobj(a):
    if(a.isnumeric()):
        return int(a)
    elif (a.isfloat()):
        return float(a)
    elif (a.bool()):
        return bool(a)
    return a
