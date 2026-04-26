"""

A -> 1

AA -> 26 + 1

BA -> 26 * 2 + 1

# 38 -> AL
# 26 * 1 + 12 
#      A + L

                         A   L     K
ALK -> 999 -> 26 * (26 * 1 + 12) + 12

999 // 26 -> 38 * 26 + 12 
1. add remainder as 12 -> K: [K]
2. check 38 > 26 -> true
3. 38 // 26 -> 1 * 26 + 12
4. add remainder as 12 -> L: [L, K]
5. check 1 > 26 -> false
6. add 1 -> A: [A, L, K]


701 // 26 -> 26 * 26 + 25 
1. add remainder as 25 -> Y: [Y]
2. check 26 > 26 -> true
3. 38 // 26 -> 1 * 26 + 12
4. add remainder as 12 -> L: [L, K]
5. check 1 > 26 -> false
6. add 1 -> A: [A, L, K]
"""
from collections import deque

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        q = deque()
        while columnNumber > 26:
            r = columnNumber % 26
            if r:
                q.appendleft(chr(ord("A") + r - 1))
            columnNumber = columnNumber // 26
        q.appendleft(chr(ord("A") + columnNumber - 1))
        s = "".join(q)
        return s
        