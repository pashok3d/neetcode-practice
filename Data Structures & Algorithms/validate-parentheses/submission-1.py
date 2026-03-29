class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in {'(', '{', '['}:
                stack.append(ch)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if ch == ")" and prev != "(":
                    return False
                if ch == "]" and prev != "[":
                    return False
                if ch == "}" and prev != "{":
                    return False
        if stack:
            return False
        return True
