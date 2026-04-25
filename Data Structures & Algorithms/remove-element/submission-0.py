class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_i = 0
        for orig_i in range(len(nums)):
            if nums[orig_i] == val:
                # skip copy
                continue
            nums[new_i] = nums[orig_i]
            new_i += 1
        return new_i
        
        