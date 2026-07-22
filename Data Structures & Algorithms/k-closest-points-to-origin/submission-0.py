class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create a max heap
        # for each point you calculate the distance and add to min heap
        # then using the k thing from the very first problem we keep appending or removing k values

        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])

        return res
