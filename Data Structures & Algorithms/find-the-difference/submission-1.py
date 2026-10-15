class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        t_freq = {}

        for ch in t:
            t_freq[ch] = t_freq.get(ch,0) + 1

        for c in s:
            t_freq[c] -= 1

        for ch in t_freq:
            if t_freq[ch] == 1:
                return ch
        