class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        freq = {}
        max_val = -1

        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        for k,v in freq.items():
            if k == v:
                max_val = max(max_val, k)

        return max_val