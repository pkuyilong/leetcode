# https://leetcode-cn.com/problems/three-consecutive-odds/


class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if not arr:
            return arr
        record = [0 for i in range(len(arr) + 1)]
        for idx in range(len(arr)):
            num = arr[idx]
            if num % 2 == 1:
                if record[idx] != 0:
                    record[idx + 1] = record[idx] + 1
                else:
                    record[idx + 1] = 1

            if record[idx + 1] == 3:
                return True
        print(record)
        return False


if __name__ == '__main__':
    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    sol = Solution()
    res = sol.threeConsecutiveOdds(arr)
    print(res)