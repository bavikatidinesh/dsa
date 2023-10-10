# Binary Search algorithm recursive way.


def binary_search_recursive(array, find_element, start, end):
    """
    This function search the element in the array in recursive way and return the index.
    if the element not found return the -1

    :param array: collection of objects
    :param find_element: search the element in the array
    :return: integer
    """
    if start <= end:
        mid = (start + end)//2
        if array[mid] == find_element:
            return mid
        elif array[mid] > find_element:
            return binary_search_recursive(array, find_element, start, mid-1)
        elif array[mid] < find_element:
            return binary_search_recursive(array, find_element, mid+1, end)
    else:
        return -1


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
        length = len(collection)
        print(binary_search_recursive(collection, 27, 0, length-1))




