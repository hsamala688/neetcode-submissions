class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == '[':
                stack.append(s[i])
            elif s[i] == "{":
                stack.append(s[i])
            elif s[i] == ')':
                if not stack:
                    return False
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif s[i] == ']':
                if not stack:
                    return False
                if stack[-1] != '[':
                    return False
                stack.pop()
            else:
                if not stack:
                    return False
                if stack[-1] != '{':
                    return False
                stack.pop()
        
        if stack:
            return False
        
        return True