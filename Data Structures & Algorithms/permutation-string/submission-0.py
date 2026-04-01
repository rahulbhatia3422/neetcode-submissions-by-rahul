class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        target = [0] * 26
        window = [0] * 26
        
        for i in range(n):
            target[ord(s1[i]) - 97] += 1
            window[ord(s2[i]) - 97] += 1

        matches = sum(1 for i in range(26) if target[i] == window[i])
        
        left = 0
        for right in range(n, m):
            if matches == 26:
                return True
            
            # Remove left
            left_idx = ord(s2[left]) - 97
            window[left_idx] -= 1
            if window[left_idx] == target[left_idx]:
                matches += 1
            elif window[left_idx] + 1 == target[left_idx]:
                matches -= 1
            left += 1
            
            # Add right
            right_idx = ord(s2[right]) - 97
            window[right_idx] += 1
            if window[right_idx] == target[right_idx]:
                matches += 1
            elif window[right_idx] - 1 == target[right_idx]:
                matches -= 1

        return matches == 26