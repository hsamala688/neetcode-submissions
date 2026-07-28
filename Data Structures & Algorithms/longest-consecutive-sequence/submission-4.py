class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for num in nums:
            if num - 1 not in seen:
                current = 1
                while num + current in seen:
                    current += 1
                longest = max(current, longest)
        return longest