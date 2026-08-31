# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        currl1 = l1
        currl2 = l2
        dummy = ListNode(0)
        curr = dummy
        while currl1 or currl2:
            val1 = currl1.val if currl1 else 0
            val2 = currl2.val if currl2 else 0
            val = (carry+val1+val2)%10
            carry = (carry+val1+val2)//10
            curr.next = ListNode(val)
            curr = curr.next
            if currl1:
                currl1 = currl1.next
            if currl2:
                currl2 = currl2.next
        if carry!=0:
            curr.next = ListNode(carry)

        return dummy.next
        