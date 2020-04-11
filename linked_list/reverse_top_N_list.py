


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = create_list(nums)
    sol = Solution()
    new_head = sol.reverseList(head, 3)
    print_list(new_head)
