class Solution:

    """
    [5, 1, 3]
    t = 3
    """
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        l = 0
        r = len(nums) - 1 # 2

        while l < r: # 0 < 1
            mid = l + (r - l) // 2 # 1
            if nums[mid] > nums[l]: # 1 > 5 false
                if nums[l] <= target and target <= nums[mid]:
                    r = mid
                else:
                    l = mid
            elif nums[mid] < nums[l]: # 1 < 5 true
                if nums[mid] <= target and target <= nums[r]: # 1 <= 3 and 3 <= 5 
                    l = mid # l = 1
                else:
                    r = mid
            else:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
                
        return mid