"""

candidates is a non-empty list of ints with duplicates

target is a positive int

find all combinations of items from candidates so
that sum(combination) == target

item can be used max once


"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def branch(cur_list: List[int], cur_idx: int):
            # check if cur_list satisfies target
            s = sum(cur_list)
            if s == target:
                result.append(cur_list.copy())
                return

            # check if cur_list overflows
            if s > target:
                return

            # check if current 
            if cur_idx >= len(candidates):
                return

            # accumulate
            instances_n = 1
            cur_cand = candidates[cur_idx]
            while cur_idx + 1 < len(candidates) and cur_cand == candidates[cur_idx + 1]:
                cur_idx += 1
                instances_n += 1
            
            # not include item at cur_idx
            branch(cur_list, cur_idx + 1)

            for n in range(1, instances_n+1):
                # include item atr cur_idx
                for _ in range(1, n+1):
                    cur_list.append(cur_cand)
                branch(cur_list, cur_idx + 1)
                for _ in range(1, n+1):
                    cur_list.pop()

        branch([], 0)
        return result



