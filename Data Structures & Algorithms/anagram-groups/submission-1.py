class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sig_to_strings_array = {}
        for s in strs:
            sig = {}
            for ch in s:
                sig[ch] = sig.get(ch, 0) + 1

            sig_hashable = frozenset(sig.items())

            if sig_hashable in sig_to_strings_array:
                sig_to_strings_array[sig_hashable].append(s)
            else:
                sig_to_strings_array[sig_hashable] = [s]
        return list(sig_to_strings_array.values())

        