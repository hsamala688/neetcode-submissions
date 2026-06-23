class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevmap = {}


        for i, n in enumerate(nums):
            complement = target - n
            if complement in prevmap:
                return [prevmap[complement], i]
            prevmap[n] = i