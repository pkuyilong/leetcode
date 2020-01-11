import numpy as np



# nums = [np.random.randint(0, 20) for _ in range(10)]

# print(nums)
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.arr = [0 for i in range(1000)] 
        self.arr = [[0 for _ in range(1000)] for _ in range(1000)]


    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        pos1 = key // 1000
        pos2 = key % 1000
        self.arr[pos1][pos2] = key
#         if key not in self.arr:
#             self.arr[key] = key


    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            pos1 = key // 1000
            pos2 = key % 1000
            self.arr[pos1][pos2] = 0
            print('remove success')
        else:
            print('no exist')

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        pos1 = key // 1000
        pos2 = key % 1000
        if self.arr[pos1][pos2] != key:
            return False
        return True

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(3)
obj.add(4)
obj.add(5)

param_5 = obj.contains(5)
print(param_5)
obj.remove(5)
param_3 = obj.contains(5)
print(param_3)
