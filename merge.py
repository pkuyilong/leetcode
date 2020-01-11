import numpy as np


# arr1 = [np.random.randint(0, 50) for _ in range(10)]
# arr2 = [np.random.randint(0, 50) for _ in range(10)]



def merge_fun(arr1, arr2):
    arr3 =[0 for i in range(len(arr1) + len(arr2))]
    i, j = 0, 0
    idx = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[idx] = arr1[i]
            i += 1
        else:
            arr3[idx] = arr2[j]
            j += 1
        idx += 1
    if i== len(arr1):
        while j < len(arr2):
            arr3[idx] = arr2[j]
            idx += 1
            j += 1

    if j== len(arr2):
        while i < len(arr1):
            arr3[idx] = arr1[i]
            idx += 1
            i += 1
    print(arr3)
    return arr3

if __name__ == '__main__':
    print('*'*80)
    arr1 = [14, 19, 1, 4, 40, 27, 1, 26, 2, 22]
    arr2 = [43, 40, 38, 15, 32, 11, 26, 8, 35, 29]
    arr1.sort()
    arr2.sort()

    arr4 = [14, 19, 1, 4, 40, 27, 1, 26, 2, 22]
    arr4.sort()
    arr4 = arr4 + arr2 + [0]*10
    print("arr4 is {}".format(arr4))
    # arr4 = arr4 + [0 for _ in range(50)]
    merge_fun2(arr4, 10, 20)








