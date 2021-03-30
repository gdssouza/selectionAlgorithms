def minimum(array):
    """
    Args:
        array (list): list with any comparable values

    Returns:
        minValue, minIndex
    """
    minValue, minIndex = array[0], 0
    for i in range(len(array)):
        if array[i] < minValue:
            minValue, minIndex = array[i], i
    return minValue, minIndex

def selectSort(array):
    """Selection sorting algorithm 

    Args:
        array (list): list with any comparable values

    Returns:
        list: ordered copy array
    """
    array = array.copy()
    n = len(array)
    for i in range(n):
        minValue, minIndex = minimum(array[i:])
        array[i+minIndex] = array[i]
        array[i] = minValue
    return array
