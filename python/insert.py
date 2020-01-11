



def ins(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 
        print(arr)



if __name__ == '__main__':
    arr = [4,3,6,8,2,1]
    ins(arr)
