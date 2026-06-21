class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        target = int(len(nums)/3)

        nums_dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        result = []

        for key, value in nums_dict.items():

                if value > target:
                    result.append(key)

        return result