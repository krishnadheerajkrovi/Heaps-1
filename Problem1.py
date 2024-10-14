'''
1. To compute the kth largest element, we are using a min heap. 
2. Iterate over the list and add values to the heap. If the length goes over k, pop the top element. 
3. We do this to only maintain the largest 2 minimum values. At the end of inserting all elements we will have the kth largest element at the top of heap.

TC: O(nlog(n-k))
SC: O(n-k)
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        pq = heapq
        li = []

        for i in range(len(nums)):
            pq.heappush(li, nums[i])
            if len(li) > k:
                pq.heappop(li)
            
        return pq.heappop(li)
