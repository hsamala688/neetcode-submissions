class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        total_len = (len(nums) + len(nums))
        result = nums + [0] * (total_len - len(nums))

        for i in range(len(result)):
            if result[i] == 0:
                result[i] = result[i - len(nums)]

        return result