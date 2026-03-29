class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = [1] # [1]
        rolling_product = 1 # 1
        for num in nums[:-1]: # [-1, 0, 1, 2]
           l2r.append(rolling_product * num)
           rolling_product = l2r[-1]

        r2l = [1]
        rolling_product = 1
        for num in nums[::-1][:-1]: # [2]
           r2l.append(rolling_product * num)
           rolling_product = r2l[-1]
        r2l = r2l[::-1]


        # l2r => [None, 0, 0]
        # r2l => [0, 1, None]
        output = []
        for l, r in zip(l2r, r2l):
            output.append(l * r)

        return output

        