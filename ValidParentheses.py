class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if (c == "[") or (c == "(") or (c == "{"):
                stack.append(c)
            if c == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            if c == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            if c == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
        return not stack