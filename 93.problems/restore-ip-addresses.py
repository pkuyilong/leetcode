# https://leetcode-cn.com/problems/restore-ip-addresses

class Solution(object):
    def restoreIpAddresses(self, s):
        tmp = list()
        ans = list()
        if s is None or len(s) < 4 or len(s) > 12:
            return ans
        self.helper(s, tmp, ans)
        ans = [".".join(ip) for ip in ans]
        return ans

    def helper(self, s, tmp, ans):
        if s == "" and len(tmp) == 4:
            ans.append(tmp[:])
            return

        # 因为每一个ip的的数据范围在0-255之间，所以做多走三次就可以了
        for i in range(min(3, len(s))):
            cur = s[:i + 1]
            # "02" "025"这样的字段是无效的，需要跳过
            if len(cur) > 1 and s[0] == '0':
                return
            if int(cur) > 255:
                return

            # 剪枝 进行加速
            if len(tmp) == 1 and len(s) > 9:
                return
            if len(tmp) == 2 and len(s) > 6:
                return
            if len(tmp) == 3 and len(s) > 3:
                return

            tmp.append(cur)
            self.helper(s[i + 1:], tmp, ans)
            tmp.pop()


if __name__ == '__main__':
    s = "25525511135"
    sol = Solution()
    ans = sol.restoreIpAddresses(s)
    print(ans)
