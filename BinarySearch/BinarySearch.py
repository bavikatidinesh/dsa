# Binary Search algorithm


def binary_search(array, find_element):
    """
    This function search the element in the array and return the index.
    if the element not found return the -1

    :param array: collection of objects
    :param find_element: search the element in the array
    :return: integer
    """
    start = 0
    end = len(array) - 1
    flag = None
    index = -1
    while start <= end:
        mid = (start + end)//2
        if array[mid] == find_element:
            flag = True
            index = mid
            break
        elif array[mid] > find_element:
            end = mid - 1
        elif array[mid] < find_element:
            start = mid + 1

    if flag:
        return index
    else:
        return index


if __name__ == "__main__":
    list1 = [[19, 27, 34, 37, 78, 134, 345, 427],
             [27, 34, 57, 897, 28],
             [1, 2, 5, 7, 8, 9, 27],
             [3, 5, 7, 27, 28, 123, 245, 400],
             [1, 2, 3, 4],
             [],
             [12, 3, 465, 67, 8, 9, 34, 456]]

    # Test the linear function
    for collection in list1:
        print(binary_search(collection, 27))


