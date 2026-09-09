# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ncount=0
        nc=head
        while nc:
            nc=nc.next
            ncount+=1

        count = right-left
        if left==1 and right!=ncount:
            prev=head
            curr=head.next
            while count>0 and curr:
                x=curr.next
                curr.next=prev
                prev=curr
                curr=x
                count-=1
            head.next=curr
            return prev

        if left==1 and right==ncount:
            prev=None
            curr=head
            while curr:
                x=curr.next
                curr.next=prev
                prev=curr
                curr=x
            return prev


        
        if head==None:
            return None
        if left==right:
            return head    
        prev=head
        curr=head
        curr=curr.next
        c=head
        for i in range(1,left-1):
            c=c.next
        for i in range(1,left):
            prev=prev.next
            curr=curr.next

        y=prev
        
        while count>0 and curr:
            x=curr.next
            curr.next=prev
            prev=curr
            curr=x
            count-=1
        y.next=curr
        c.next=prev
        return head


        


        
        
        