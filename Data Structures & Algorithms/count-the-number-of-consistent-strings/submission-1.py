class Solution:
    def countConsistentStrings(self, allowed, words):
        count = 0

        for word in words:
            if all(ch in allowed for ch in word):
                count += 1

        return count