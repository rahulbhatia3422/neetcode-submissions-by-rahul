import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        minCapital = []

        for c, p in zip(capital, profits):
            heapq.heappush(minCapital, (c, p))

        maxProfit = []

        for _ in range(k):

            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)

            if not maxProfit:
                break

            w += -heapq.heappop(maxProfit)

        return w
        