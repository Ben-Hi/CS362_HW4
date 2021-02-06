# Generates a full name from a first string and last string

def fullname(first, last):
    if first is not str or last is not str:
        raise TypeError

    else:
        return first + " " + last