# write a python program to find whether a given string has balanced parentheses or not.

def Check_balanced(s1):
    """
    This method checks the if the string is balanced parentheses or not.
    :param s1: string
    :return: bool
    """
    stack = []
    dict1 = {"}": '{', ")": '(', "]": "["}

    for item in s1:
        if item in dict1.keys():
            if len(stack) > 0 and stack[-1] == dict1[item]:
                stack.pop()
            else:
                return False
        else:
            stack.append(item)

    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    print("{[]{()}} :", Check_balanced("{[]{()}}"))
    print("()[]{} :", Check_balanced("()[]{}"))
    print("[{}{})(] :", Check_balanced("[{}{})(]"))
    print("((()[][]))] :", Check_balanced("((()[][]))]"))
    print("[((()[][]))] :", Check_balanced("[((()[][]))]"))
    print("[[[((()[][]))]] :", Check_balanced("[[[((()[][]))]]"))
    print("[(()[]{})] :", Check_balanced("[(()[]{})]"))