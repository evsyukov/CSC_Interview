import sys


def main():
    reader = (line.split() for line in sys.stdin)
    q = int(input())
    stack_max = [0]
    for _ in range(q):
        command = next(reader)
        if command[0] == "push":
            stack_max.append(max(stack_max[-1], int(command[1])))
        elif command[0] == "pop":
            del stack_max[-1]
        else:
            print(stack_max[-1])


if __name__ == "__main__":
    main()
