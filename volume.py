#Calculate the volume of a cube

def cube_validation(l, w, h):


def volume(l, w, h):
    if l is str or w is str or h is str:
        raise TypeError
    
    elif l <= 0 or w <= 0 or h <= 0:
        raise Exception("Invalid Cube Dimensions")

    else:
        return l * w * h