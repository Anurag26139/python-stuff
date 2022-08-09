class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=d=ListNode(0)
        d.next=head
        while d.next and d.next.next:
            p=d.next
            q=d.next.next
            d.next,p.next,q.next=q,q.next,p
            d=p
        return temp.next