class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x

        while left < right:
            mid = left + (right - left) // 2
            
            if (mid * mid) >= x:
                right = mid
            else:
                left = mid + 1
        return left if left * left == x else left - 1
