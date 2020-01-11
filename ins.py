import numpy as np





def ins(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    print(arr)


if __name__ == '__main__':
    arr = [np.random.randint(0,30) for i in range(30)] 
    ins(arr)
