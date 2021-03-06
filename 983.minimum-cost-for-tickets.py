# 983. 最低票价
# https://leetcode-cn.com/problems/minimum-cost-for-tickets/


# class Solution(object):
#     def mincostTickets(self, days, costs):
#         if days is None or len(days) == 0 or costs is None or len(costs) == 0:
#             return 0
#         daysets = set(days)
#         dp = [0 for i in range(days[len(days) - 1] + 1)]
#         for i in range(1, len(dp)):
#             if i not in daysets:
#                 dp[i] = dp[i - 1]
#             else:
#                 # 如果要出行，肯定需要票，可能是1日票，7日票， 30日票
#                 n1 = dp[i - 1] + costs[0]
#                 n2 = costs[1] + dp[i - 7] if i >= 7 else costs[1]
#                 n3 = costs[2] + dp[i - 30] if i >= 30 else costs[2]
#                 dp[i] = min(n1, n2, n3)
#         return dp[-1]


class Solution:
    def mincostTickets(self, days, costs):
        if len(days) == 0 or len(costs) == 0:
            return 0
        dp = [0 for _ in range(days[-1] + 1)]
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                # 7天之内的可能买一个星期的票更合适
                if i <= 7:
                     dp[i] = min(costs[1], dp[i-1] + costs[0])
                # 30天之内的可能买一个月的票更合适
                elif i <= 30:
                    dp[i] = min(dp[i-7] + costs[1], costs[2], dp[i-1] + costs[0])
                else:
                     dp[i] = min(dp[i-7] + costs[1], dp[i-30] + costs[2], dp[i-1] + costs[0])
        print(dp)
        return dp[-1]



if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    sol = Solution()
    res = sol.mincostTickets(days, costs)
    print(res)
