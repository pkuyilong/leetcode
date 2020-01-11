class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None:
            return 0
        idx = 0
        for num in nums:
            if num != val:
                nums[idx] = num
                idx += 1
        return idx

    def removeElement2(self, nums, val):
        if nums is None:
            return 0
        count = 0
        for idx in range(len(nums)):
            if nums[idx] == val:
                i = idx
                while i < len(nums) - 1:
                    nums[i] = nums[i+1]
                    i += 1
            else:
                count += 1
            print(nums)
        return count


    def removeElement3(self, nums, val):
        if nums is None:
            return 0
        '''
        set save num but no count
        '''
        s = set()
        d = dict()

        for item in nums:
            if item != val:
                d[item] = d.get(item, 0) + 1
                s.add(item)
        # d is list after sorted 
        d = sorted(d.items(), key=lambda x: x[0])
        print(type(d))
        x = dict(d)
        print(x)
        return len(d)



if __name__ == "__main__":
    print('*'*80)
    sol = Solution()
    nums = [3, 0, 2, 2, 5, 4, 4, 2]
    res = sol.removeElement3(nums, 2)
    print(res)
