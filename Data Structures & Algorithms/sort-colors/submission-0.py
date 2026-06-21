class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def heapify(length: int, root_index: int) -> List[int]:

            curr = root_index

            while True:
                largest = curr
                left = 2 * curr + 1
                right = 2 * curr + 2

                if left < length and nums[left] > nums[largest]:
                    largest = left

                if right < length and nums[right] > nums[largest]:
                    largest = right

                if largest == curr:
                    break

                nums[curr], nums[largest] = nums[largest], nums[curr]

                curr = largest
            
        for i in range(n // 2, -1, -1):
            heapify(n, i)
        
        for i in range( n - 1, 0 , -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)

        return nums