class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cur = 0

        for num in nums:
            if num == 0:
                res = max(cur, res)
                cur = 0
            else:
                cur += 1

        return max(cur, res)

