class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        
        count = 0

        for ch in s:
            if ch == " ":
                count = 0
            
            else:
                count += 1

        return count
        