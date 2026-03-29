class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[tuple[int, int]] = []
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_lower_i, _ = stack.pop()
                output[prev_lower_i] = i - prev_lower_i
            stack.append((i, temp))
        return output
