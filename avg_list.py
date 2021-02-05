# Calculate average of elements in a list

def avg_list(elements):
    if isinstance(elements, list):
        sum = 0
        count = 0

        for element in elements:
            sum += element
            count += 1
        
        return sum / count

    else:
        raise TypeError