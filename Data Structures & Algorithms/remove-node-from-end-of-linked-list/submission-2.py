# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return None
        
        len_n = 0
        cur = head
        while cur:
            len_n += 1
            cur = cur.next
        idx_to_remove = len_n - n

        cur = head
        cur_idx = 0
        if idx_to_remove > 0:
            while cur:
                if cur_idx + 1 == idx_to_remove:
                    cur.next = cur.next.next
                cur = cur.next
                cur_idx += 1
        else:
            head = head.next
        return head
        
        



        