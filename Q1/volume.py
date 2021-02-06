#Calculate the volume of a cube
def volume(l, w, h):
    if isInt(l) != True and isFloat(l) != True:
        raise TypeError
    
    elif isInt(w) != True and isFloat(w) != True:
        raise TypeError

    elif isInt(h) != True and isFloat(h) != True:
        raise TypeError

    elif l <= 0 or w <= 0 or h <= 0:
        return -1

    # Volume Calculation
    else:
        return l * w * h


# Input Validation
def isInt(x):
    if type(x) == int:
        return True
    else:
        return False

def isFloat(x):
    if type(x) == float:
        return True
    else:
        return False