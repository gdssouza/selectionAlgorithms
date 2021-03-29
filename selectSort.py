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
    for i in range(len(array)):
        minValue, minIndex = minimum(array[i:])
        array[i+minIndex] = array[i]
        array[i] = minValue
    return array

# array original
array = [5, 4, 6, 2, 1, 7, 0, 3, 8, 9]
# resultado
array_select = selectSort(array)
# gabarito
gabarito = array.copy()
gabarito.sort()

# saida
print("Array Original: ", array)
print("Array Select:   ", array_select)
print("Array Gabarito: ", gabarito)
