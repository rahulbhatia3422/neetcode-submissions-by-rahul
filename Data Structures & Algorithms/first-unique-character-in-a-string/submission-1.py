class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq_map = {}

        for ch in s:

            freq_map[ch] = freq_map.get(ch, 0) + 1

        for k,v in freq_map.items():

            if v == 1:
                return s.index(k)

        return -1
        