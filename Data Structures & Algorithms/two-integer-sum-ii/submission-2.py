class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while r - l - 1 >= 0:
            cur = numbers[r] + numbers[l]
            if cur == target:
                return [l+1, r+1]
            elif cur > target:
                # reduce by moving right pointer
                r -= 1
            else:
                l += 1
            