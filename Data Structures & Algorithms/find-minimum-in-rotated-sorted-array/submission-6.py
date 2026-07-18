class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]

        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]
        
        while left <= right:

            mid = left + (right - left) // 2

            res = min(res, nums[mid])

            if nums[mid] < nums[right]:

                right = mid - 1

            else:

                left = mid + 1

        return res
            