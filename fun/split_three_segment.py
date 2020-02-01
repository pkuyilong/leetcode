


class Solution():
    def split_segment(self, num, k):
        tmp = []
        tmp_count = 0
        self.helper(num, k, tmp_count, tmp)

    def helper(self, num, k, tmp_count, tmp):
        if num < 0 or tmp_count > k:
            return
        if tmp_count == k and num == 0:
            print(tmp)
            return

        for i in range(1, num+1):
            tmp.append(i)
            # print(tmp)
            self.helper(num - i, k, tmp_count + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    sol = Solution()
    sol.split_segment(8, 3)









