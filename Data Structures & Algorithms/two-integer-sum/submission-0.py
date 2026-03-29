class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary dict[int, int], where
        # value is the last index of target - key value
        # in nums
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            d[target - num] = i
        
        
        