# BubbleSort is a sorting algorithm


def bubble_sort(array):
    """
    this method is to sort the array in ascending order.

    :param array:
    :return: sorted array
    """
    size = len(array)

    for i in range(size-1):

        swapped = False
        for j in range(0, size-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True

        if not swapped :
            break


if __name__ == "__main__":
    list1 = [[19, 27, 34, 37, 78, 134, 345, 427],
             [27, 34, 57, 897, 28],
             [5, 7, 8, 9, 1, 2,  27],
             [123, 245, 400,3, 5, 7, 27, 28, 100],
             [1, 2, 3, 4, 9, 7],
             [],
             [12, 3, 465, 67, 8, 9, 34, 456]]

    # Test the linear function
    for collection in list1:
        print("Before sorting:", collection)
        bubble_sort(collection)
        print("After sorting:", collection)







