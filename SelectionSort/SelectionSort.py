# selection Sort is a sorting algorithm


def selection_sort(array):
    """
    this method is to sort the array in ascending order.

    :param array:
    :return: sorted array
    """

    size = len(array)

    for i in range(size):
        min_id = i
        for j in range(i, size):
            if array[j] < array[min_id]:
                min_id = j

        array[i], array[min_id] = array[min_id], array[i]


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
        selection_sort(collection)
        print("After sorting:", collection)
