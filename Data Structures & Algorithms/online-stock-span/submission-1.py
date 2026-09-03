class StockSpanner:
    # Keep a monotonic decreasing stack for the prices of the stock each day
    # When the next price is higher than the top, we pop until it is not
    # Along the way, for each popped price add its span to the current days span
    # Intuition is that if price i is in j's span, i's span will also be in j's span
    # Return the span of the current price
    # time complexity: O(n) each element is pushed or popped at most twice where n = # calls to next
    # space complexity: O(n) worst case the price continues to decrease for n days
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        price_span = 1
        if self.stack:
            while self.stack and self.stack[-1][0] <= price:
                _, span = self.stack.pop()
                price_span += span
        self.stack.append((price, price_span))
        return price_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)