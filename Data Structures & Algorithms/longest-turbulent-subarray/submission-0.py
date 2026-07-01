class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n
        
        max_len = 0
        curr_len = 0
        prev_sign = -1  # -1: none, 0: up, 1: down
        
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:      # Down
                curr_len = curr_len + 1 if prev_sign == 0 else 1
                prev_sign = 1
            elif arr[i] < arr[i + 1]:    # Up
                curr_len = curr_len + 1 if prev_sign == 1 else 1
                prev_sign = 0
            else:                         # Equal
                curr_len = 0
                prev_sign = -1
            
            max_len = max(max_len, curr_len)
        
        return max_len + 1 if max_len > 0 else 1