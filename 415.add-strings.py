# class Solution(object):
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         if len(num1) == 0 and len(num2) == 0:
#             return "0"
#         if len(num1) == 0 or len(num2) == 0:
#             return num2 if len(num1) == 0 else num1
#
#         num1_length = len(num1)
#         num2_length = len(num2)
#         num1_list = list(num1)[::-1]
#         num2_list = list(num2)[::-1]
#         num_list = list()
#
#         # 进位
#         carry = 0
#         i = 0
#         # for i in range(min(num1_length, num2_length)):
#         while i < min(num1_length, num2_length):
#             tmp = int(num1_list[i]) + int(num2_list[i]) + carry
#             ans = tmp % 10
#             carry = 1 if tmp >= 10 else 0
#             num_list.insert(0, str(ans))
#             i += 1
#
#         if i == num1_length and i == num2_length:
#             if carry:
#                 num_list.insert(0, "1")
#             return "".join(num_list)
#
#         if i == num1_length:
#              j = i
#              while j < num2_length:
#                 tmp = int(num2_list[j]) + carry
#                 ans = tmp % 10
#                 carry = 1 if tmp >= 10 else 0
#                 num_list.insert(0, str(ans))
#                 j += 1
#         else:
#             j = i
#             while j < num1_length:
#                 tmp = int(num1_list[j]) + carry
#                 ans = tmp % 10
#                 carry = 1 if tmp >= 10 else 0
#                 num_list.insert(0, str(ans))
#                 j +=1
#
#         if carry:
#             num_list.insert(0, "1")
#         return "".join(num_list)

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        list1 = list(num1)[::-1]
        list2 = list(num2)[::-1]
        result = list()
        carry = 0
        i = 0
        while i < min(l1, l2):
            tmp = int(list1[i]) + int(list2[i]) + carry
            ans = tmp % 10
            carry = 1 if tmp >= 10 else 0
            result.insert(0, str(ans))
            i += 1

        if i == l1 and i != l2:
            j = i
            while j < l2:
                tmp = int(list2[j]) + carry
                ans = tmp % 10
                carry = 1 if tmp >= 10 else 0
                result.insert(0, str(ans))
                j += 1
        elif i == l2 and i != l1:
            j = i
            while j < l1:
                tmp = int(list1[j]) + carry
                ans = tmp % 10
                carry = 1 if tmp >= 10 else 0
                result.insert(0, str(ans))
                j += 1
        if carry:
            result.insert(0, "1")
        return "".join(result)


if __name__ == '__main__':
    num1 = "98"
    num2 = "9"
    sol = Solution()
    res = sol.addStrings(num1, num2)
    print(res)