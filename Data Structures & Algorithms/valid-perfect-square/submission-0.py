import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = int(math.sqrt(num))
        return root * root == num
        