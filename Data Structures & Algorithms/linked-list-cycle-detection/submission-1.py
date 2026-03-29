# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        visited = set()
        cur = head
        while cur:
            if cur.next in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False