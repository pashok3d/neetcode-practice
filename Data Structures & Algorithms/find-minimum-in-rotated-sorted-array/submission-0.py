class Solution:
    """
    [6, 1, 2, 3, 4, 5]
    [5, 6, 1, 2, 3, 4]
    [4, 5, 6, 1, 2, 3]
    [3, 4, 5, 6, 1, 2]
    """
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]

        while len(nums) > 2:
            mid = len(nums)//2
            if nums[mid] > nums[0]:
                # min is smwhere in nums[mid:]
                nums = nums[mid:]
            else:
                # min is smwhere in nums[:mid+1]
                nums = nums[:mid+1]
        return nums[1]
        
        