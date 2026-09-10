# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        x=head
        count=0
        if head==None or head.next==None:
            return head
        while x:
            count+=1
            x=x.next
        if count==k:
            return head

        if count<k:
            k=k %count
        
        for i in range(1,k+1):
            first=head
            prev=head 
            curr=head.next
            
            while curr and curr.next:
                curr=curr.next
                prev=prev.next
            curr.next=first
            prev.next=None
            first=curr
            head=first
        return head
        