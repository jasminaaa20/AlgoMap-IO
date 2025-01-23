class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0

        if len(s) <= 0: return True

        while j < len(t):
            if t[j] == s[i]:
                i += 1
                if i == len(s):
                    return True
            j += 1
        
        return False
