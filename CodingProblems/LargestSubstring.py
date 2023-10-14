# Python program that finds the longest substring without repeating characters

def findSubString(s):
    """
    this method is to find the largest substring with out repeating the char

    :param s: input string
    :return int: large substring length
    """
    if not s or len(s) <= 0:
        return 0
    i = 0
    j = 0
    max_len = 0
    stack = []
    while i < len(s):
        while s[i] in stack:
            stack.pop(0)
            j += 1
        stack.append(s[i])
        max_len = max(max_len, i - j + 1)

        i += 1
    return max_len


if __name__ == "__main__":
    list1 = ["dinesh", "aba", "  ", "", "abccdddefs", "abccedf", "z"]

    # Test the linear function
    for collection in list1:
        length = findSubString(collection)
        print(f"for the {collection} substring length {length}")