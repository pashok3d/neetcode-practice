class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_i = 0
        for orig_i in range(len(nums)):
            if num_orig_at_i := nums[orig_i]:
                nums[new_i] = num_orig_at_i
                new_i += 1
            
        while new_i < len(nums):
            nums[new_i] = 0
            new_i += 1
        