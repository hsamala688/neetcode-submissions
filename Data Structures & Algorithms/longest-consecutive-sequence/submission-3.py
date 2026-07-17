class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        all_nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in all_nums:
                current = 1
                while num + current in all_nums:
                    current += 1

                longest = max(current, longest)
        
        return longest