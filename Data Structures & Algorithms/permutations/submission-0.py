class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        
        nums_set = set(nums)
        results = []

        def step(cur_nums_set: Set[int], cur_nums_set_len: int, rolling_permulation: List[int]):
            if cur_nums_set_len <= 0:
                results.append(rolling_permulation.copy())
                return
            for num in list(cur_nums_set): # 1 | 2 
                # take num, append to rolling parmutation
                # run step with set of remaining nums 
                cur_nums_set.remove(num) # {2, 3} | {3} | {}
                rolling_permulation.append(num) # [1] | [1, 2] | [1, 2, 3]
                step(cur_nums_set, cur_nums_set_len - 1, rolling_permulation) # step({2,3}, 2, [1]) | step({3}, 1, [1, 2])
                rolling_permulation.pop() # [1]
                cur_nums_set.add(num) # {3, 2}

        step(nums_set, len(nums_set), [])
        return results