from collections import defaultdict
class FreqStack:
    # The approach to this problem is to recognize that this is not a standard LIFO stack
    # Hence we don't need a single list to keep account of all items pushed and pop the last one pushed
    # To keep track of the max frequency element we could keep track with a heap that sorts by occurance and last index
    # This would however require keeping a stack structure to keep track of the indices for each element and many heappushes
    # A better approach, would be to keep account of the max frequencies across the stack
    # We have a dictionary that has the count for an element as the key and that count points to a running list of elements that occur that many times across the stack
    # We also know which stack to push an element in using a second counter dictionary that counts an elements occurances
    # We also have the max key from this dictionary as a variable to keep track of the max frequency across the stack
    # This solves the toughest problems of the problem. Keep track of the max frequency element and cases where there's a tie and we need the most recent element
    # When we need the max_frequency value we can pop() the last element in freq_dict[max_freq] which will either be a lone element or the most recent of multiple
    # Time complexity: O(1) for push, O(1) for pop
    # Space complexity: O(N) worst case all values are pushed to the dictionaries

    def __init__(self):
        self.counter = defaultdict(int)
        self.freq_map = defaultdict(list)
        self.max_freq = -(float("inf"))

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.freq_map[self.counter[val]].append(val)
        self.max_freq = max(self.max_freq, self.counter[val])

    def pop(self) -> int:
        res = self.freq_map[self.max_freq].pop()
        self.counter[res] -= 1
        if not self.freq_map[self.max_freq]:
            self.max_freq -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()