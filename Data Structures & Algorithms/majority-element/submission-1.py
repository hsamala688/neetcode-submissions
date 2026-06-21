class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        nums_dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        return max(nums_dict, key=nums_dict.get)
        """

        result = count = 0
        
        for num in nums:
            if count == 0:
                result = num
            if num == result:
                count += 1
            else:
                count -= 1
        
        return result