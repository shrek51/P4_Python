from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isParenthesis(c):
            return ((c == '(') or (c == ')'))

        def isValidString(str):
            cnt = 0
            for i in range(len(str)):
                if (str[i] == '('):
                    cnt += 1                    # if its opening bracket then push it
                elif (str[i] == ')'):
                    cnt -= 1                    # if its closing bracket then pop it
                if (cnt < 0):
                    return False
            return (cnt == 0)

        if (len(s) == 0):
            return []

        visit = set()           # visit set to ignore already visited 
        q = []                                
        result = []
        level = 0

        q.append(s)              # append the character of string s to queue 'q'
        visit.add(s)
        while(len(q)):
            s = q[0]
            q.pop(0)
            if (isValidString(s)):
                result.append(s)
                level = True        # If answer is found, make level true so that valid of only that level are processed
            if (level):
                continue
            for i in range(len(s)):
                if (not isParenthesis(s[i])):
                    continue
                temp = s[0:i] + s[i + 1:] 
                if temp not in visit:    #again repeating the process with the one that are not visited.
                    q.append(temp)
                    visit.add(temp)
        return result