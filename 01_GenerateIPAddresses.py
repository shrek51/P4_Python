class Solution:
    
    def check(self, s):
        n = len(s)
        if n < 1 or n > 3:
            return False
        if s[0] == "0" and n > 1:
            return False
        p = int(s)
        if p < 0 or p > 255:
            return False
        return True

    def generate(self, s, n, i, j, k):
        s1 = s[:i+1]        # Substring from the start to i (inclusive)
        s2 = s[i+1:j+1]     # Substring from i+1 to j (inclusive)
        s3 = s[j+1:k+1]     # Substring from j+1 to k (inclusive)
        s4 = s[k+1:]        # Substring from k+1 to the end of the string
        if self.check(s1) and self.check(s2) and self.check(s3) and self.check(s4):
            return s1 + "." + s2 + "." + s3 + "." + s4
        return ""

    def genIp(self, s):
        ans = []
        n = len(s)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    st = self.generate(s, n, i, j, k)
                    if st:
                        ans.append(st)
        return ans