# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find the middle
        l1, l2 = head,head.next
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        
        curr1 = head
        curr2 = l1.next
        l1.next = None

        #Reverese Second List
        curr2 = self.reverseList(curr2)

        while curr2:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next = curr2
            curr1 = temp1
            curr2.next = curr1
            curr2 = temp2

        return 
    
    def reverseList(self,head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next =  prev
            prev = curr
            curr = temp
        return prev
        
        


        