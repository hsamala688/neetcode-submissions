class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums_set = set()

        for i in range(len(nums)):

            val = nums[i]

            if val in nums_set:

                return True
            
            nums_set.add(val)

        return False