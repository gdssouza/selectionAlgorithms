def bubbleSort(array):
    """Bubble sorting algorithm 

    Args:
        array (list): list with any comparable values

    Returns:
        list: ordered copy array
    """
    array = array.copy()
    n = len(array)
    sort = False
    while not sort:
        sort = True
        for i in range(n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sort = False
    return array
