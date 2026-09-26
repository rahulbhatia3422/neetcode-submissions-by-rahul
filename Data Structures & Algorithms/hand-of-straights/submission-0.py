from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in sorted(count):  # process in ascending order
            while count[num] > 0:  # try to start a group at num
                for i in range(num, num + groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1
        return True
