class Solution:

    def encode(self, strs: List[str]) -> str:
        return strs.__repr__()

    def decode(self, s: str) -> List[str]:
        return eval(s)