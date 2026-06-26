class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}

        for num in nums:

            hash_map[num] = hash_map.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for num, frequency in hash_map.items():

            buckets[frequency].append(num)

        res = []

        for i in range(len(buckets) - 1, 0 , -1):

            for num in buckets[i]:

                res.append(num)

                if len(res) == k:

                    return res