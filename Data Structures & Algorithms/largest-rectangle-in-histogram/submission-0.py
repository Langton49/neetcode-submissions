class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Intuition: a small height will act as a bottleneck to the area of any rectange between i and j
        # Because of this we can keep a monotonic increasing stack for the heights
        # This is because if we find a height lower than the previous, no rectangle can be formed after bigger than it
        # Thus when we find a smaller height we can find the maximum area before this point and keep track of the largest
        # We pop and evaluae the area backwards as long as the current element is smaller than the top
        # When we are finished we have to evaluate the remaining heights which will be strictly increasing
        # This is to check for areas where the width is large

        stack = [-1]
        n = len(heights)
        idx = 0
        max_area = 0

        while idx < n:
            while stack[-1] != -1 and heights[idx] <= heights[stack[-1]]:
                i = stack.pop()
                max_area = max(max_area, (idx-stack[-1]-1) * heights[i])
            stack.append(idx)
            idx += 1
        
        while stack[-1] != -1:
            i = stack.pop()
            max_area = max(max_area, (idx-stack[-1]-1) * heights[i])

        return max_area