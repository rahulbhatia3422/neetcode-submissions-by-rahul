class Solution:
    def maxDifference(self, s: str) -> int:
        freq_map = {}

        odd = 0
        max_odd = float('-inf')

        even = 0
        min_even = float('inf')

        for ch in s:
            freq_map[ch] = freq_map.get(ch,0) + 1

        for value in freq_map.values():
            
            if value % 2 == 0:
                even = value

                if even < min_even:
                    min_even = even

            else:

                odd = value
                if odd > max_odd:
                    max_odd = odd

        return max_odd - min_even