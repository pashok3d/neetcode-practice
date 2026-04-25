class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n_pointer = 0
        prev = None
        for o_pointer in range(len(nums)):
            if nums[o_pointer] != prev:
                nums[n_pointer] = nums[o_pointer]
                n_pointer += 1
            prev = nums[o_pointer]
        return n_pointer
        