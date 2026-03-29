class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                right_operand = stack.pop()
                left_operand = stack.pop()
                result = eval(f"{left_operand}{token}{right_operand}")
                stack.append(int(result))
            else:
                stack.append(int(token))
        return stack[-1]