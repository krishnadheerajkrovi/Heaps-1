'''
1. Insert into a heap the nodes value and the node itself. Write a custom less than func for the ListNode comparisions.
2. Have a dummy node at the beginning of the list. As long as the heap is not empty, pop an element from it - append to the cur node and push the next node of it into the heap if it exists.
3. Since it is a heap, the nodes are rearranged to a minheap after every insert
3. Return the next node of dummy which is the beginning of the sorted list.

TC: O(nklogk)
SC: O(k)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        pq = heapq
        li = []
        dummy = ListNode(-sys.maxsize-1)
        cur = dummy 
        ListNode.__lt__  = lambda x,y : x.val < y.val
        for l in lists:
            if l:
                pq.heappush(li, (l.val, l))
        
        while len(li) > 0:
            val, Min = pq.heappop(li)
            cur.next = Min
            if Min.next != None:
                pq.heappush(li, (Min.next.val, Min.next))
            cur = cur.next 
        
        return dummy.next
        









        