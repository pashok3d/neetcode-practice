class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def func(cur_list: List[int], cur_index):
            if cur_index == len(nums):
                result.append(cur_list.copy())
                return
            func(cur_list, cur_index + 1)
            cur_list.append(nums[cur_index])
            func(cur_list, cur_index + 1)
            cur_list.pop()

        func([], 0)
        return result

