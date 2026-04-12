"""
height array is at least 2 items

height = [3,2,10,10,2,1]

two pointers approach
start from both ends
move pointers - which one? on what condition?
"""



class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0
        while r - l - 1 >= 0:
            water = min(heights[r],heights[l]) * (r - l)
            max_water = max(max_water, water)
            if heights[l] < heights[r]:
                # move l
                l += 1
            else:
                r -= 1
            
        return max_water