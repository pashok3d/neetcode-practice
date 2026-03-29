class Solution:
    """
    [-1, 0, 1, 2]
    """
    def search(self, nums: List[int], target: int) -> int:
        shift = 0
        while nums:
            split_index = len(nums) // 2
            if nums[split_index] == target:
                return split_index + shift
            elif target < nums[split_index]:
                nums = nums[:split_index]
            elif target > nums[split_index]:
                nums = nums[split_index+1:]
                shift += split_index + 1
        return -1