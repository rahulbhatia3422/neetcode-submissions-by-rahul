from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        return [num for num, count in freq.items() if count == 1]