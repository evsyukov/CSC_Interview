def sift_down(a, i, size, m_list):
    min_index = i
    l = 2*i + 1
    if l <= size - 1 and a[l] < a[min_index]:
        min_index = l
    r = 2*i + 2
    if r <= size - 1 and a[r] < a[min_index]:
        min_index = r
    if i != min_index:
        m_list.append([i,min_index])
        a[i], a[min_index] = a[min_index], a[i]
        sift_down(a, min_index, size, m_list)


def build_heap(a, n, m_list):
    size = n
    for i in range(n//2 - 1, -1, -1):
        sift_down(a, i, size, m_list)


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    m_list = []
    build_heap(a, n, m_list)
    print(len(m_list))
    for x in range(len(m_list)):
        print(m_list[x][0], m_list[x][1])


if __name__ == "__main__":
    main()
