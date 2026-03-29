class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        sorted_d_iter = iter(sorted(d.items(), key=lambda x: x[1], reverse=True))
        return [next(sorted_d_iter)[0] for i in range(k)]
