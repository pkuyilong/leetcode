# 46. 全排列
# https://leetcode-cn.com/problems/permutations/

from queue import Queue


class Solution:
    """ 大致思路
    1.  将中间结果缓存到队列中
    2.  对中间结果的各个位置插入新来的值组成新的结果，跟新到队列中
    3.  重复处理


    具体例子
    1. 先处理第一个数字，那么就是a，放到一个list中,成了[[a]]
    2. 如果再来一个数字b，从队列中取出[a], 在其左边和右边插入数字，得到了[ba] 和  [ab]，list更新为[[ba], [ab]]
    3. 如果再来一个数字c, 那么依次从list中取出元素
        3.1 首先取出的是ba， 然后在ba的前边、中间以及后边插入c，变成了 ==>> [cba]，[bca]，[bac]
        3.2 再取出的是ab, 然后在ab的前边、中间以及后边插入c，变成了   ==>> [cab], [acb], [abc]
        3.3 更新list
    4. 重复执行即可
    """
    def permute(self, nums):
        if nums is None or len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums]

        q = Queue()
        result = []

        for num in nums:
            size = q.qsize()
            while size:
                arr = q.get()
                for i in range(len(arr) + 1):
                    # prevent insert function from changing origin list, use shallow copy
                    tmp_arr = arr.copy()
                    tmp_arr.insert(i, num)

                    # print(tmp_arr)
                    # if all num that in nums used, find a result
                    if len(tmp_arr) == len(nums):
                        result.append(tmp_arr)
                    q.put(tmp_arr)
                size -= 1
            else:
                q.put([num])
        # print(result)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))