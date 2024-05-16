class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def isAllStars(S1, i):
            # Helper function to check if all characters up to index i in S1 are '*'
            for j in range(i):
                if S1[j] != '*':
                    return False
            return True

        n = len(s)
        m = len(p)

        # Initialize two lists, prev and cur, to store the previous and current rows of the DP array
        prev = [True] + [False] * m

        for i in range(1, m + 1):
            if p[i - 1] == '*':
                prev[i] = prev[i - 1]
        
        for i in range(1, n + 1):
            cur = [False] * (m + 1)
            for j in range(1, m + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    cur[j] = prev[j - 1]
                elif p[j - 1] == '*':
                    cur[j] = prev[j - 1] or prev[j] or cur[j - 1]
            prev = cur
        
        return prev[m]

# Example usage:
# sol = Solution()
# print(sol.isMatch("aa", "*"))  # Expected output: True
