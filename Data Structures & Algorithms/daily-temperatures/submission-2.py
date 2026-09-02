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

        for i in range(n-2, -1, -1):
            if temperatures[i] < temperatures[i+1]:
                res[i] = 1
            else:
                k = i + 1
                while res[k] and k < n:
                    k += res[k]
                    if temperatures[i] < temperatures[k]:
                        res[i] = k - i
                        break
        return res