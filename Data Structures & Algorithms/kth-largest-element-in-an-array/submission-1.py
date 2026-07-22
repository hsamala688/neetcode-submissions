class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, num)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        maxHeap.append(0)
        return (maxHeap[0])