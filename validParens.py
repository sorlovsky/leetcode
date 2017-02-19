def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        if ch == "[":
            stack.append(ch)
        if ch == "{":
            stack.append(ch)

        if ch == ")":
            if len(stack) == 0:
                return False
            if stack[len(stack)-1] != "(":
                return False
            else:
                stack.pop()

        if ch == "]":
            if len(stack) == 0:
                return False
            if stack[len(stack)-1] != "[":
                return False
            else:
                stack.pop()

        if ch == "}":
            if len(stack) == 0:
                return False
            if stack[len(stack)-1] != "{":
                return False
            else:
                stack.pop()


    if len(stack) == 0:
        return True
    return False

def main():
    print(isValid("["))
    print("hello")
main()
