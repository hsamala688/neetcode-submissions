class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        res = nums[0]

        left = 0 

        right = len(nums) - 1

        while left <= right:

            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = left + (right - left) // 2

            res = min(res, nums[mid])

            if nums[mid] < nums[right]:

                right = mid - 1

            else:

                left = mid + 1

        return res
        '''

        for i in range(len(nums)):

            if nums[i] == target:

                return i

        return -1