def is_balanced(s):
    stack = []
    index = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.insert(0, s[i])
            index.insert(0, i)
        elif s[i] == ')' or s[i] == ']' or s[i] == '}':
            if not stack:
                return i + 1
                # return False
            top = stack.pop(0)
            trash = index.pop(0)
            if (top == '[' and s[i] != ']' ) or \
                    (top == '(' and s[i] != ')') or \
                    (top == '{' and s[i] != '}'):
                return i + 1
                # return False
    if not stack and not index:
        return 0
    else:
        return index[0] + 1
    # return not stack


def main():
    s = [x for x in input()]
    t = is_balanced(s)
    if not t:
        print("Success")
    else:
        print(t)
    # print(t)


if __name__ == "__main__":
    main()