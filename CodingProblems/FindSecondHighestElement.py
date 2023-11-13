# Find the second highest element from the list in O(n)
import unittest


def findSecondHighestElement(list1):
    """
    To find the Second Highest Element from the list
    """
    first_highest = second_highest = float('-inf')

    for element in list1:
        if first_highest < element:
            second_highest = first_highest
            first_highest = element
        elif second_highest < element and element != first_highest:
            second_highest = element

    return second_highest


class TestSecondHighestElementFunctionality(unittest.TestCase):
    """
    To test the functionality of the Second Highest Element from the list
    """

    def testStartingSecondHighestElement(self):
        list1 = [10, 6, 8, 39, 4, 9, 3, 1, 2, 7]
        second_element = findSecondHighestElement(list1)
        self.assertEqual(second_element, 10)

    def testEndSecondHighestElement(self):
        list1 = [-2, 6, 8, 39, 4, 9, 3, -1, 2, 7, 11]
        second_element = findSecondHighestElement(list1)
        self.assertEqual(second_element, 11)

    def testMiddleSecondHighestElement(self):
        list1 = [-2, 6, 8, 39, 9, 3, -1, 2, 7, 40]
        second_element = findSecondHighestElement(list1)
        self.assertEqual(second_element, 39)

    def testNegativeSecondHighestElement(self):
        list1 = [-2, -6, -8, -39, 0, 1, -1, -12, -3]
        second_element = findSecondHighestElement(list1)
        self.assertEqual(second_element, 0)


if __name__ == "__main__":
    # main method starts
    unittest.main()