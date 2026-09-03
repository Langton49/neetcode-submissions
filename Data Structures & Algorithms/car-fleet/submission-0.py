class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # For a fleet to form a fast car has to be behind a slow car or rather a car has to cover the remaining distance to target in a lower time than a car ahead of it
        # To do that we can get the time it takes for a car to reach target and determine whether thats slower than any car before it whichi it would form a fleet with
        # To do that efficiently the position array has to be sorted and we use a stack to form fleets by popping cars before current car that are faster
        # By the end the number of fleets is the same as the len(stack)
        # Time: O(nlogn) the algorithm takes O(n) but the sorting O(nlogn) overpowers that
        # Space: O(n) worst case all times get pushed to stack

        sorted_idx = sorted(range(len(position)), key=position.__getitem__)
        stack = []
        for idx in sorted_idx:
            time = (target - position[idx]) / speed[idx]
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)