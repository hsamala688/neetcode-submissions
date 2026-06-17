class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [0] * n

        for i in range(n):
            current_product = 1
            for j in range(n):
                if i != j:
                    current_product *= nums[j]
            output[i] = current_product
        
        return output

            





