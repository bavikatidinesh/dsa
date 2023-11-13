# Find the second smallest element from the list in O(n)
import unittest


def findSecondSmallestElement(list1):
    """
    To find the Second Smallest Element from the list
    """
    first_highest = second_highest = float('inf')

    for element in list1:
        if first_highest > element:
            second_highest = first_highest
            first_highest = element
        elif second_highest > element != first_highest:
            second_highest = element

    return second_highest


class TestSecondSmallestElementFunctionality(unittest.TestCase):
    """
    To test the functionality of the Second Smallest Element from the list
    """

    def testStartingSecondSmallestElement(self):
        list1 = [2, 6, 8, 39, 4, 9, 3, 1, 12, 7]
        second_element = findSecondSmallestElement(list1)
        self.assertEqual(second_element, 2)

    def testEndSecondSmallestElement(self):
        list1 = [-2, 6, 8, 39, 4, 9, 3, -1, 2, 7, -11, -9]
        second_element = findSecondSmallestElement(list1)
        self.assertEqual(second_element, -9)

    def testMiddleSecondSmallestElement(self):
        list1 = [-2, 6, 8, 39, 9, -1, 2, 7, 40]
        second_element = findSecondSmallestElement(list1)
        self.assertEqual(second_element, -1)

    def testNegativeSecondSmallestElement(self):
        list1 = [-2, -6, -8, -39, 0, 1, -1, -12, -3]
        second_element = findSecondSmallestElement(list1)
        self.assertEqual(second_element, -12)

    def testNegativeTestSecondSmallestElement(self):
        list1 = [-2, -6, -8, -39, 0, 1, -1, -12, -3]
        second_element = findSecondSmallestElement(list1)
        self.assertNotEqual(second_element, -6)


if __name__ == "__main__":
    # main method starts
    unittest.main()
