class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # This is just binary search honestly, you know how it is done
        # Have two pointers at the ends of the list
        # Calculate a middle pointer and depending on where the target is, update the search range
        # Keep going until you find target
        # Time complexity: O(logn) the space to be searched is cut in half each time
        # Space complexity: O(1) no extra memory needed
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1