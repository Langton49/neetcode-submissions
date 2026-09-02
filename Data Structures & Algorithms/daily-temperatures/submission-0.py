class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Init an array of size n with all 0s
        # Init a stack that will maintain a decreasing order (we only add values less than top and when a value higher appears, pop until the top is greater than the current value)
        # Intuition: The stack wil keep indices of the values in temperatures and if we only pop when we see a higher value, the difference between the current index and the top will be the days before we saw a value higher than top
        # The difference is written to the initialized default array and returned as the result
        # Time complexity: O(N) each value is pushed and popped at most twice so its linear
        # Space complexity: O(N) worst case all values are dcreasing and the stack contains all values at the end

        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                val = stack.pop()
                res[val] = i - val
            stack.append(i)
        return res