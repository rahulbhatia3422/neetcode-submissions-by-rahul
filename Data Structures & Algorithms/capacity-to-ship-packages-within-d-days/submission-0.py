class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_ship(capacity):
            """
            Check if we can ship all packages within 'days' days
            using a ship with given capacity
            """
            # Start with first day, first package
            current_load = 0  # Weight loaded on current day
            days_needed = 1    # At least 1 day needed
            
            for weight in weights:
                # If adding this package exceeds capacity, start a new day
                if current_load + weight > capacity:
                    days_needed += 1      # Need another day
                    current_load = weight # Start new day with this package
                    
                    # Early exit: if we already need more days than allowed
                    if days_needed > days:
                        return False
                else:
                    # Add package to current day
                    current_load += weight
            
            return True
        
        # Binary search boundaries
        left = max(weights)    # Lower bound: can't ship the heaviest package
        right = sum(weights)   # Upper bound: ship everything in one day
        
        # Binary search for minimum capacity that works
        while left < right:
            mid = (left + right) // 2
            
            if can_ship(mid):
                # This capacity works, try to find smaller capacity
                right = mid
            else:
                # This capacity doesn't work, need larger capacity
                left = mid + 1
        
        return left