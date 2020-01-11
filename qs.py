




if __name__ == '__main__':
    l = [5, 17, 12, 6, 7, 2, 10]
    key = l[0]
    i = 0
    j = len(l) - 1
    while i < j:
        while i < j and l[j] > key:
            j -= 1
        if i < j:
            l[i], l[j] = l[j], l[i]

        while i < j and  l[i] < key:
            i += 1
        if i < j:
            l[i], l[j] == l[j], l[i]
    print("i, j is {} {}".format(i, j))
    print(l)
