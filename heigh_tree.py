def height(child, v):
    stack_first = [v]
    stack_second = []
    h = 0
    while stack_first != []:
        stack_second = [x for x in stack_first]
        stack_first = []
        for ver in stack_second:
            for each in child[ver]:
                stack_first.append(each)
        h += 1
    return h


def main():
    n = int(input())
    r = [int(x) for x in input().split()]
    child = [[] for x in range(n)]
    v = float('-inf')
    for x in range(n):
        if r[x] == -1:
            v = x
            continue
        child[r[x]].append(x)
    print(height(child, v))


if __name__ == "__main__":
    main()