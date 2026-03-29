# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
h -> n1 -> n2 -> n3
h n1 -> n2 -> n3
  ^

h <- n1 <- n2 <- n3
n3 -> n2 -> n1 -> h
return n3
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        current = head
        while current.next is not None:
            next_node = current.next # 1
            current.next = prev # h -> None
            prev = current # prev := h
            current = next_node # current := n1

        current.next = prev

        return current
        