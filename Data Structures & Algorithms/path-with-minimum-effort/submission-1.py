import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        visited = set()
        heap = [(0, 0, 0)]  # effort_to_add_cell, row, col
        max_effort = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))
            max_effort = max(max_effort, diff)

            if r == rows - 1 and c == cols - 1:
                return max_effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                ):
                    edge_diff = abs(heights[r][c] - heights[nr][nc])
                    heapq.heappush(heap, (edge_diff, nr, nc))

        return max_effort