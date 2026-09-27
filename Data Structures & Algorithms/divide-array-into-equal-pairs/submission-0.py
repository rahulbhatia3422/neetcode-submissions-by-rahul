class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1

        for v in freq_map.values():
            if v % 2 != 0:
                return False
        
        return True