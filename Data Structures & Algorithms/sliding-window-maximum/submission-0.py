from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        output = []
        q = deque()  # store indices
        
        for i in range(len(nums)):
            # Remove indices from back while their values < current
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            
            # Remove front if it's outside window: window = [i-k+1, i]
            if q[0] == i - k:
                q.popleft()
            
            # Add to output once window size is reached
            if i >= k - 1:
                output.append(nums[q[0]])
        
        return output