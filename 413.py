# class Solution(object):
#     def numberOfArithmeticSlices(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         ans = []
#         if A is not None and len(A) < 3:
#             return 0
#         length = len(A)
#         dp = [[False for i in range(length)] for i in range(length)]
#
#         # 先把三个可以构成等差数列的给算出来, 因为最有一组是从倒数第三个(length -3)为开始位置, 也就是
#         # 右侧不可取到的边界就是length - 2
#         for i in range(length - 2):
#             if A[i+1] - A[i] == A[i+2] - A[i+1]:
#                 dp[i][i+2] = True
#                 ans.append(A[i: i+3])
#
#         for i in range(length - 2):
#             for j in range(i, length):
#                 if j - i + 1 > 3:
#                     if dp[i][j-1]:
#                         if A[j] - A[j-1] == A[i+1] - A[i]:
#                             dp[i][j] = True
#                             ans.append(A[i: j+1])
#         return len(ans)

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        count = 0
        for i in range(len(A) - 3 + 1):
            dis = A[i + 1] - A[i]
            for j in range(i + 2, len(A)):
                if A[j] - A[j - 1] == dis:
                    count += 1
                else:
                    break
        return count


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    sol = Solution()
    res = sol.numberOfArithmeticSlices(A)
    print(res)
