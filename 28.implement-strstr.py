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
