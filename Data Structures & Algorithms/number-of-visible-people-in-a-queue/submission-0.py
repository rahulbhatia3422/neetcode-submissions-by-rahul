class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        ans = [0] * n
        stack = []

        # iterate from right to left
        for i in range(n-1, -1, -1):

            count = 0

            # pop all smaller heights (visible)
            while stack and heights[i] > stack[-1]:

                stack.pop()
                count += 1
                
            # if stack still has someone taller, count him too
            if stack:
                count += 1
            ans[i] = count
            stack.append(heights[i])
        return ans
