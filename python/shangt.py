from collections import defaultdict




if __name__ == '__main__':
    l = [0, 0, 1, 1, 0, 1, 1, 1, 0]
    print(l)
    l = [ -1  if x == 0 else 1 for x in l]
    print(l)
    for i in range(1, len(l)):
        l[i] = l[i] + l[i-1]
    print(l)
    for i in range(len(l) -1, -1, -1):
        if l[i] == 0:
            print(i)

    # d = defaultdict(int)
    # for i in range(len(l)):
    #     d[l[i]] = i;
    # res = 0
    # ans = []
    # print(d)
    # for i in range(len(l)):
    #     if l[i] in d.keys():
    #         print(d[l[i]] - i)
    #         tmp = d[l[i]] - i
    #         if tmp > res:
    #             res = tmp
    #             ans = [i, d[l[i]]]
    # print(ans)
