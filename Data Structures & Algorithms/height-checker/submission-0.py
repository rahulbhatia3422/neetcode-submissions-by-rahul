class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        i = 0
        while i < len(heights):
            if heights[i] != expected[i]:
                count += 1
            i += 1
        return count