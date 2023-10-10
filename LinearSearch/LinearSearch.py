# linear search algorithm without using the builtin functions
# simplest searching algorithm.
# start from one end and check every element of the list until the last element


def linear_search(array, find_element):
    """
    This function search the element in the array and return the index.
    if the element not found return the -1

    :param array: collection of objects
    :param find_element: search the element in the array
    :return: integer
    """
    index = 0
    flag = None

    for obj in array:
        if obj == find_element:
            flag = True
            break
        index += 1

    if flag:
        return index
    else:
        return -1



if __name__ == "__main__":
    list1 = [[19, 34, 5, 78, 34, 345, 27],
         [27, 34, 57, 897, 28],
         [1, 200, 45, 56, 78, 27, 24],
         [3, 5, 7, 27, 23, 1, 245],
          [1, 2, 3, 4],
         [],
         [12, 3, 465,67, 8,9, 34,456]]

    # Test the linear function
    for collection in list1:
        print(linear_search(collection, 27))
    print("*"*20)

    list2 = [["rajesh","raj", "ram", "amay", "remo"],
             ["raj", "ram", "amay", "rajesh", "remo", "jani"],
             ["raj", "ram", "amay", "remo", "rajesh"],
             [],
             ["raj", "ram", "amay", "remo"]
             ]

    # Test the linear function
    for collection in list2:
        print(linear_search(collection, "rajesh"))


