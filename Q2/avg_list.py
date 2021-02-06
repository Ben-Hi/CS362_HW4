# Calculate average of elements in a list

def avg_list(elements):
    if isinstance(elements, list):
        # Empty List case
        if len(elements) == 0:
            return 0

        sum = 0
        count = 0

        for element in elements:
            if type(element) != int and type(element) != float:
                raise TypeError
            else:
                sum += element
                count += 1
        
        return sum / count

    else:
        raise TypeError