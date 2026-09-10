# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        count=0
        curr=head
        while curr :
            curr=curr.next
            count+=1
        if count==1:
            return head

        if count ==2:
            left=head
            right=head.next
            right.next=left
            head=right
            left.next=None
            return head
            
        if count%2==0 and count!=2:
            left =head
            right=head.next
            x=right.next
            right.next=left
            y=left
            head=right
            left=x
            right=left.next
            y.next=right
            while right.next and right.next.next:
                x=right.next
                right.next=left
                y=left
                left=x
                right=left.next
                y.next=right
            right.next=left
            left.next=None
        else:
            left =head
            right=head.next
            x=right.next
            right.next=left
            y=left
            head=right
            left=x
            right=left.next
            y.next=right
            while right:
                x=right.next
                right.next=left
                y=left
                left=x
                right=left.next
                y.next=right
            y.next=left
            left.next=None
            
            

                
        return head

        
        