


class Solution():
    def split_segment(self, num, k):
        tmp = []
        final = []
        tmp_count = 0
        self.helper(num, k, tmp_count, tmp, final)
        return final

    def helper(self, num, k, tmp_count, tmp, final):
        if num < 0 or tmp_count > k:
            return
        if tmp_count == k and num == 0:
            final.append(tmp[:])
            return final

        for i in range(1, num+1):
            if len(tmp) and i < tmp[-1]:
                continue
            tmp.append(i)
            self.helper(num - i, k, tmp_count + 1, tmp, final)
            tmp.pop()


if __name__ == '__main__':
    sol = Solution()
    res = sol.split_segment(8, 3)
    print(res)









