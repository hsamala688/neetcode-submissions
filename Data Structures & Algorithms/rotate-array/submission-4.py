class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        left = 0
        right = k

        while right < len(nums):

            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right += 1

        return nums
        '''
        counter = 0

        while counter < k:
            nums.insert(0, nums.pop())
            counter += 1

        return nums
