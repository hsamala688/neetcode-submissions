class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x

        while left <= right:

            val = (left + right) // 2

            if val*val == x:

                return val

            elif val*val > x:

                right = val - 1

            else:

                left = val + 1

        return right