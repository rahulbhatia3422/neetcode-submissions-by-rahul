class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(number):

            # Helper function: calculates sum of squares of digits
            # Example: for 19 -> 1² + 9² = 1 + 81 = 82

            return sum(int(digit) ** 2 for digit in str(number))

        # Initialize two pointers
        slow = n                # Slow pointer moves 1 step at a time
        fast = get_next(n)      # Fast pointer moves 2 steps at a time


            # Continue until fast reaches 1 or pointers meet (cycle detected)

        while fast != 1 and slow != fast:
            slow = get_next(slow)              # Move slow pointer 1 step
            fast = get_next(get_next(fast))    # Move fast pointer 2 steps

        # If fast reached 1, it's happy; otherwise, it's not

        return fast == 1

        
        