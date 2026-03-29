# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        q1 = list1 if list1.val <= list2.val else list2
        q2 = list2 if list1.val <= list2.val else list1
        
        head = q1
        cur = head

        q1 = q1.next

        while q1 or q2:
            if q1 and q2:
                if q1.val <= q2.val:
                    cur.next = q1
                    cur = cur.next
                    q1 = q1.next
                else:
                    cur.next = q2
                    cur = cur.next
                    q2 = q2.next
            elif q1:
                cur.next = q1
                break
            elif q2:
                cur.next = q2
                break
        return head
        
