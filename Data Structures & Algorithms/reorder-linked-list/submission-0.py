# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
[2, 4, 6, 8]
    s  f
       s
          c 

2 -> 4 -> 6 -> None
8 -> None
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            slow = slow.next 
        
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        right = prev
        left = head

        """
        l: 2 -> 4 -> 6 -> None
        r: 8 -> None
        """

        while right: # 8
            left_next_tmp = left.next # 4
            left.next = right # 2 -> 8
            
            right_next_tmp = right.next # None
            right.next = left_next_tmp # 8 -> 4
            right = right_next_tmp # None
            left = left_next_tmp # 4
            
            
    



