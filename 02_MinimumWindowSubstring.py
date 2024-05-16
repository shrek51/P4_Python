class Solution(object):
    def minWindow(self, s, t):
        if len(t) == 0:
            return ""
        
        mpt = {}
        mps = {}
        for char in t:
            mpt[char] = mpt.get(char, 0) + 1
        
        cur = 0
        total = len(mpt)
        i = 0
        j = 0
        res = float('inf')
        indices = (0, 0)
        
        while j < len(s):
            if s[j] in mpt:
                mps[s[j]] = mps.get(s[j], 0) + 1
                if mps[s[j]] == mpt[s[j]]:
                    cur += 1
            
            while cur == total:
                if j - i + 1 < res:
                    res = j - i + 1
                    indices = (i, j)
                
                if s[i] in mps:
                    mps[s[i]] -= 1
                    if mps[s[i]] < mpt[s[i]]:
                        cur -= 1
                i += 1
            j += 1
        
        if res == float('inf'):
            return ""
        
        return s[indices[0]:indices[1]+1]
