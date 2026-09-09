# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return None
        
        prev=head
        curr=head.next
        while curr:
            if curr.val==val:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=prev.next
                curr=curr.next
        if head.val==val:
            head=head.next
        return head


        