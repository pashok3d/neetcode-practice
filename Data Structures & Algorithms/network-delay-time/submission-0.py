import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adjacency list
        nodes = defaultdict(list)
        for u, v, t in times:
            nodes[u].append((v, t))
        max_time = -1
        heap = [[0, k]]
        visited = set()

        while heap: 
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            n -= 1
            max_time = max(max_time, time)

            for nei, time_to_nei in nodes[node]:
                if nei in visited:
                    continue
                heapq.heappush(heap, [time + time_to_nei, nei])

        if n:
            return -1
        else:
            return max_time

