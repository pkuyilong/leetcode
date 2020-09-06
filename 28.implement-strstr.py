class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None:
            return -1
        if  needle == "":
            return 0
        for i in range(len(haystack)):
            j = 0
            while j < len(needle):
                if i+j == len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    break
                j +=1
            if j == len(needle):
                return i
        return -1


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None:
            return -1
        if needle == "":
            return 0

        ### 最有一个有意义的位置: len(stack) - 1  - len(needle) + 1
        ### 然后还要 + 1 (最有的一个+1是因为要放在range里面, 不然最有一个有意义的位置取不到)
        for i in range(len(haystack) - len(needle) + 1):
            # 这个j是为了遍历needle而准备的
            j = 0
            while j < len(needle):
                if haystack[i+j] != needle[j]:
                    break
                j +=1
            if j == len(needle):
                return i
        return -1