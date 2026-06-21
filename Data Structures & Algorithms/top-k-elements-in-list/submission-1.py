class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        sorted_nums = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)
        
        result = []

        for i in range(k):
            result.append(sorted_nums[i][0])

        return result
        