class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for efficient binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        left, right = 0, m
        
        while left <= right:
            # Partition point for nums1
            i = (left + right) // 2
            # Partition point for nums2 (remaining elements needed)
            j = half - i
            
            # Handle edge cases with -inf and +inf
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Valid partition found
            if left1 <= right2 and left2 <= right1:
                # Even total length
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                # Odd total length
                else:
                    return min(right1, right2)
            
            # Adjust binary search
            elif left1 > right2:
                # Too many elements from nums1, move left
                right = i - 1
            else:
                # Too few elements from nums1, move right
                left = i + 1
        
        # Should never reach here with valid input
        return 0.0