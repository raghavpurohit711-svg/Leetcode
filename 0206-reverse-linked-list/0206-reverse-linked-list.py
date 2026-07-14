# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals=[]
        curr = head
        while curr:
            vals.append(curr.val)
            curr=curr.next
        vals = vals[::-1]
        dummy = ListNode()
        curr = dummy
        for x in vals:
            curr.next = ListNode(x)
            curr = curr.next
        head = dummy
        return dummy.next