class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Gonna use the upper bound binary search algorithm
        # The upper bound search looks at the maximum value where the target can be found or inserted into the list
        # With two pointers at the ends of the list one will be an index outside the list
        # We perform normal binary search but skip the check for nums[mid] == target
        # When the pointers become equal eventually, the loop breaks and we return one of them as the result
        # Time complexity: O(logn) cutting the search space in half each time
        # Space complexity: O(1) no extra space needed
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left