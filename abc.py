class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        arr=[]
        while cur:
            arr.append(cur.val)
            cur=cur.next
        arr[k-1] ,arr[-k] = arr[-k],arr[k-1]
        dummy= cur = ListNode(0)
        for a in arr:
            cur.next=ListNode(a)
            cur=cur.next
        return dummy.next