class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        # brute force
        n = len(nums)
        output = [0] * n

        for i in range(n):
            current_product = 1
            for j in range(n):
                if i != j:
                    current_product *= nums[j]
            output[i] = current_product
        
        return output
        '''

        # O(N) time baby:

        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1 , -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output

    

            





