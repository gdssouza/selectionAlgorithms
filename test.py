from selectSort import selectSort
from bubbleSort import bubbleSort

def main():
    # array original
    array = [5, 4, 6, 2, 1, 7, 0, 3, 8, 9]
    # resultados
    array_select = selectSort(array)
    array_bubble = bubbleSort(array)
    # gabarito
    gabarito = array.copy()
    gabarito.sort()

    # saidas
    print("Array Original: ", array)
    print("Array Select:   ", array_select)
    print("Array Bubble:   ", array_bubble)
    print("Array Gabarito: ", gabarito)

if __name__ == "__main__":
    main()