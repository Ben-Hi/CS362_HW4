#Calculate the volume of a cube

def volume(l, w, h):
    # Input Validation
    if l is str or w is str or h is str:
        raise TypeError
    
    elif type(l) == bool or type(w) == bool or type(h) == bool:
        raise TypeError

    elif l <= 0 or w <= 0 or h <= 0:
        return -1

    # Volume Calculation
    else:
        return l * w * h