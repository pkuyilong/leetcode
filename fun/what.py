
class Solution:
    sucessor = 0


    def change(self):
        self.sucessor = 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.sucessor)
    print(sol.change())
    print(sol.sucessor)
    print(Solution().sucessor)

