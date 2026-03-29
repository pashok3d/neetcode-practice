class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums_set:
                current_num = num
                length = 0
                while current_num in nums_set:
                    length += 1
                    current_num += 1
                longest = max(longest, length)
        return longest

