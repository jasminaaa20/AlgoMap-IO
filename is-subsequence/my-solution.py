class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == 0: return True

        i = 0
        for letter in t:
            if letter == s[i]:
                i += 1
                if i == len(s):
                    return True
        
        return False

        # Time Complexity: O(T)
        # Space Complexity: O(1)
