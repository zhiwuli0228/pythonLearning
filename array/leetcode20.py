class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char_s in s:
            if char_s == '(' or char_s == '[' or char_s == '{':
                stack.append(char_s)
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if char_s == ')' and temp != '(':
                    return False
                if char_s == ']' and temp != '[':
                    return False
                if char_s == '}' and temp != '{':
                    return False
        return len(stack) == 0
