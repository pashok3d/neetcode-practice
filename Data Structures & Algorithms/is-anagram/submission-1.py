class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        for ch in s:
            s_chars[ch] = s_chars.get(ch, 0) + 1
        t_chars = {}
        for ch in t:
            t_chars[ch] = t_chars.get(ch, 0) + 1

        return t_chars == s_chars
        