class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for c in s:
            if c in valid:
                top_element = stack.pop() if stack else '#'

                if valid[c] != top_element:
                    return False
            else:
                stack.append(c)
        
        return not stack
