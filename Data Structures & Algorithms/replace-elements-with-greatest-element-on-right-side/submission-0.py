class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        length = len(arr)

        ans = [0] * length

        max_el = -1

        for i in range(length  - 1, -1, -1):
            ans[i] = max_el
            max_el = max(arr[i], max_el)
        
        return ans