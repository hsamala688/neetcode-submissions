class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + [0] * len(nums)
        for i in range(len(ans)):
            if ans[i] == 0:
                ans[i] = ans[i - len(nums)]
        return ans