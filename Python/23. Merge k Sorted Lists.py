class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        res = ListNode([])

        while len(lists) > 1:
            if not lists[0]:
                del lists[0]
                continue
            if not lists[1]:
                del lists[1]
                continue
            tail = res

            while lists[1] and lists[0]:
                if lists[1].val >= lists[0].val:
                    tail.next = ListNode(lists[0].val)
                    lists[0] = lists[0].next
                else:
                    tail.next = ListNode(lists[1].val)
                    lists[1] = lists[1].next
                
                tail = tail.next
                if not lists[0]:
                    tail.next = lists[1]
                if not lists[1]:
                    tail.next = lists[0]

            lists[0] = res.next
            del lists[1]
        return lists[0]