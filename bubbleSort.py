def bubbleSort(array):
    """Bubble sorting algorithm 

    Args:
        array (list): list with any comparable values

    Returns:
        list: ordered copy array
    """
    n = len(array)
    sort = False
    while not sort:
        sort = True
        for i in range(n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sort = False
    return array

# array original
array = [5, 4, 6, 2, 1, 7, 0, 3, 8, 9]
# gabarito
gabarito = array.copy()
gabarito.sort()
# resultado
array_bubble = bubbleSort(array)

# saida
print("Array Original:  ", array)
print("Array Gabarito:  ", gabarito)
print("Array Bubble:    ", array_bubble)
