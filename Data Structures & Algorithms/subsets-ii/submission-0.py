"""
[1, 2, 1]

[1, 2]
[2, 1]


[1, 1, 2]
[1, 2]
[1, 1, 2]
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        nums_len = len(nums)

        def step(current_nums: List[int], idx: int):
            if idx == nums_len: # 0 == 3
                results.append(current_nums.copy())
                return

            next_idx = idx + 1 # 1
            dups = 1
            while next_idx < nums_len and nums[idx] == nums[next_idx]:
                # duplicates at [idx, idx+1, ...]
                next_idx += 1
                dups += 1 

            # nums: [1, 1, 2]
            # idx: 0
            # dups: 2
            # next_idx: 2
            step(current_nums, next_idx) # step([], 2)

            for _ in range(dups):
                current_nums.append(nums[idx])
                step(current_nums, next_idx) # step([1], 2)

            for _ in range(dups):
                current_nums.pop()
        
        step([], 0)

        return results