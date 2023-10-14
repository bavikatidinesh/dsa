# merge Sort is a sorting algorithm


def merge_sort(array):
    """
    this method is to sort the array in ascending order.

    :param array:
    :return: sorted array
    """

    if len(array) > 1:

        end = len(array)

        mid = end//2

        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


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
        merge_sort(collection)
        print("After sorting:", collection)