import numpy as np


# 执行过程
"""
nums = [17, 15, 9, 4, 8, 2, 15, 0, 11, 4]

Front:  [17]
Behind:  [15]
Ret: [15, 17] 

Front:  [15, 17]
Behind:  [9]
Ret: [9, 15, 17] 

Front:  [4]
Behind:  [8]
Ret: [4, 8] 

Front:  [9, 15, 17]
Behind:  [4, 8]
Ret: [4, 8, 9, 15, 17] 

Front:  [2]
Behind:  [15]
Ret: [2, 15] 

Front:  [2, 15]
Behind:  [0]
Ret: [0, 2, 15] 

Front:  [11]
Behind:  [4]
Ret: [4, 11] 

Front:  [0, 2, 15]
Behind:  [4, 11]
Ret: [0, 2, 4, 11, 15] 

Front:  [4, 8, 9, 15, 17]
Behind:  [0, 2, 4, 11, 15]
Ret: [0, 2, 4, 4, 8, 9, 11, 15, 15, 17] 

[0, 2, 4, 4, 8, 9, 11, 15, 15, 17]

"""

class Merge():
    def merge_sort(self, nums):
        if nums is None or len(nums) == 0 or len(nums) == 1:
            return nums
        return self.merge_sort_worker(nums)

    def merge_sort_worker(self, nums):
        if len(nums) <= 1:
            return nums
        # split
        mid = len(nums) >> 1
        # 这里如果选择mid+1，那么会一直无限循环
        front = self.merge_sort_worker(nums[:mid])
        behind = self.merge_sort_worker(nums[mid:])
        # merge
        print("Front: ", front)
        print("Behind: ", behind)
        ret = self.merge_worker_1(front, behind)
        print("Ret: {} \n".format(ret))
        return ret

    def merge_worker(self, front, behind):
        new_nums = [None for i in range(len(front) + len(behind))]
        i, j = 0, 0
        idx = 0
        while i < len(front) and j < len(behind):
            if front[i] < behind[j]:
                new_nums[idx] = front[i]
                i += 1
            else:
                new_nums[idx] = behind[j]
                j += 1
            idx += 1

        while i < len(front):
            new_nums[idx] = front[i]
            idx += 1
            i += 1

        while j < len(behind):
            new_nums[idx] = behind[j]
            idx += 1
            j += 1
        return new_nums

    def merge_worker_1(self, front, behind):
        new_nums = []
        i, j = 0, 0
        while i < len(front) and j < len(behind):
            if front[i] < behind[j]:
                new_nums.append(front[i])
                i += 1
            else:
                new_nums.append(behind[j])
                j += 1
        # python_version 化的写法，比较简洁
        new_nums += front[i:]
        new_nums += behind[j:]
        return new_nums


if __name__ == '__main__':
    nums = [17, 15, 9, 4, 8, 2, 15, 0, 11, 4]
    sol = Merge()
    ret = sol.merge_sort(nums)
    print(ret)

