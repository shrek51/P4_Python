class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matching_bracket = {')': '(', '}': '{', ']': '['}  
        stack = []

        for char in s:
            if char in matching_bracket:
                top_element = stack.pop() if stack else '#'  # "#" is a dummy value assigned if no matching brackets are found
                if matching_bracket[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack  # return true if the stack is empty
