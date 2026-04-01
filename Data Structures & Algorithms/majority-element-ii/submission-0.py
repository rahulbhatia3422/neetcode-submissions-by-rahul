class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = {}
        result = []
        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1

        for k, v in freq_map.items():
            if v > len(nums) // 3:

                result.append(k)
        return result
        