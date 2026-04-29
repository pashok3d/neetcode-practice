import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # start at first point
        # visited set is initialized with start point

        # neigbours are all the rest of the points except for visited
        # put neighbours in heap
        # pop from heap
        # move to poped, mark as visited

        def manhattan(i: tuple[int, int], j: tuple[int, int]) -> int:
            return abs(i[0] - j[0]) + abs(i[1] - j[1])

        heap = [(0, (points[0][0], points[0][1]))]
        not_visited = set((point[0], point[1]) for point in points)
        total_cost = 0

        while heap:
            cost, point = heapq.heappop(heap)
            if point not in not_visited:
                continue
            not_visited.remove(point)
            total_cost += cost
            for nei in not_visited:
                cost_to_nei = manhattan(point, nei)
                heapq.heappush(heap, (cost_to_nei, nei))

        return total_cost





        