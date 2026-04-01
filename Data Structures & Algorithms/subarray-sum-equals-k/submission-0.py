class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        # Map: prefix_sum -> frequency
        sum_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            # If (prefix_sum - k) exists in map, we found subarrays
            needed = prefix_sum - k
            if needed in sum_count:
                count += sum_count[needed]
            
            # Update frequency of current prefix sum
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        return count