class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_i = 0
        for orig_i in range(len(nums)):
            num_orig = nums[orig_i]
            if num_orig == val:
                # skip copy
                continue
            nums[new_i] = num_orig
            new_i += 1
        return new_i
        
        