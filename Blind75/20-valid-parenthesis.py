class Solution:
    def isValid(self, s: str) -> bool:
        # use stack data structure to store the data
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char) # put into stack
            else:
                if len(stack) == 0 or stack[-1] != char: # check if it's the same as the last one in stack
                    return False
                else:
                    stack.pop()
        return True if not stack else False
