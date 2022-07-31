class Solution:
    def mergeTwoLists(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        temp=ListNode()
        final=temp
        while l1 and l2:
            if l1.val<l2.val:
                final.next=l1
                l1=l1.next
            else:
                final.next=l2
                l2=l2.next
            final=final.next
        if l1:
            final.next=l1
        elif l2:
            final.next=l2
        return temp.next