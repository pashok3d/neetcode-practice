"""
abcbc
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        seen_chars = {}
        l = r = 0
        longest = 1
        while r < len(s): # r = 4
            char_that_r_points_at = s[r] # b
            if char_that_r_points_at in seen_chars:
                desired_l = seen_chars[char_that_r_points_at] + 1
                while l < desired_l:
                    seen_chars.pop(s[l])
                    l += 1
            else:
                longest = max(longest, r - l + 1) # 3
            seen_chars[char_that_r_points_at] = r # {a: 0, b:1, c:2}
            r += 1 

        return longest
        