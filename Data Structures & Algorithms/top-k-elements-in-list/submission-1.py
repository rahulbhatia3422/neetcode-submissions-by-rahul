class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        # Sort items by frequency in descending order and take first k
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        
        # Return just the keys (numbers) of the k most frequent items
        return [item[0] for item in sorted_items[:k]]