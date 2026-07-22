class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones] #have to do this because we are setting up a max Heap
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])