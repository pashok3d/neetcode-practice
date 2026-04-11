"""

 [1, 1, 3, 3]
1:x  -  *  *  
2:-  *  *  * 

@cache
def dp(index: int):
    # stop condition / base case
    if index == len(nums) - 1:
        return nums[index]
    
    if index > len(nums) - 1::
        return 0

    return max(nums[index] + dp(index+2), dp(index+1))

dp(0)
"""


from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def dp(index: int) -> int:
            # stop condition / base case
            if index == len(nums) - 1:
                return nums[index]
            
            if index > len(nums) - 1:
                return 0

            return max(nums[index] + dp(index+2), dp(index+1))

        return dp(0)
        
        