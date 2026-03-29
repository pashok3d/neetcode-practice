class Solution:
    """
    abba
    0123
     12

    """
    def isPalindrome(self, s: str) -> bool:

        def is_alpha_numeric(ch: str):
            if ord(ch) <= 57 and ord(ch) >= 48:
                return True
            if ord(ch) <= 122 and ord(ch) >= 65:
                return True
            return False

        s = "".join([ch for ch in s if is_alpha_numeric(ch)]).lower()
        l_to_r_pointer = 0
        r_to_l_pointer = len(s) - 1
        while l_to_r_pointer < r_to_l_pointer:
            if s[l_to_r_pointer] != s[r_to_l_pointer]:
                return False
            l_to_r_pointer += 1
            r_to_l_pointer -= 1
        return True
        

        