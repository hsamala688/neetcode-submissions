class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        '''
        if the value is below 0 ignore it

        else lets say you take the given array and then sort through it an add a value 0 to a spot where it is missing

        sorting is going to cost an

        I think I got it

        we are going to scan once, if we move through and we see that the next value is not x + 1, we mark with an n

        '''


        n = len(nums)
        i = 0

        while i < n:
            if nums[i] <= 0 or nums[i] >n:
                i += 1
                continue

            index = nums[i] - 1

            if nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]

            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

        
