from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        Format: length + '#' + string
        """
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string back to a list of strings."""
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i = i + length
        return res