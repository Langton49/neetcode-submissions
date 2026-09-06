class Solution:
    def decodeString(self, s: str) -> str:
        # To decode a string, it would be better to decode from the inside-out rather than progressively with the string
        # To achieve this behavior, a suggested approach is to use recursion where the algorithm goes as deep as possible and decodes the inner most string
        # The decoded inner string gets iteratively added to a string variable that will be decoded as well
        # If the the iterative section encounters a lone letter, it just gets added to the result as well
        # Time complexity: O(N) each character will be read once
        # Space complexity: O(N) although the only auxiliary space used is for the result, function calls get stored to the call stack and worst case it could be O(N)
        n = len(s)
        res = ""
        i = 0
        def build_substring(m: int, start: int) -> str:
            res = ""
            if start >= n:
                return res
            while start < n and s[start] != ']':
                if s[start].isnumeric():
                    rep = ""
                    while s[start].isnumeric():
                        rep += s[start]
                        start += 1
                    inner_substring, next_idx = build_substring(int(rep), start+1)
                    res += inner_substring
                    start = next_idx
                else:
                    res += s[start]
                start += 1
            return m * res, start
        
        while i < n:
            if s[i].isnumeric():
                m = ""
                while s[i].isnumeric():
                    m += s[i] 
                    i += 1
                inner_substring, next_idx = build_substring(int(m), i+1)
                res += inner_substring
                i = next_idx
            else:
                res += s[i]
            i += 1
        return res



                