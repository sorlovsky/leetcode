def subset(s):
    subsets = []
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            subsets.append(s[i:j])
    return subsets
    
def unique(s):
    # chs = ""
    # for ch in s:
    #     if ch in chs:
    #         return False
    #     chs+=ch
    # return True
    return len(set(s)) == len(s)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        return len(max(filter(unique, subset(s)), key=len))
