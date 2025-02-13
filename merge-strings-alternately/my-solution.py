class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n1, n2 = len(word1), len(word2)
        merged = []

        for i in range(max(n1, n2)):
            if i < n1:
                merged.append(word1[i])
            if i < n2:
                merged.append(word2[i])
        
        return "".join(merged)
        # Time complexity: O(n1+n2)
        # Space complexity: O(n1+n2)
        
