import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict

        # Step 1: Build adjacency list
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Min Heap -> (current_distance, node)
        minHeap = [(0, k)]

        # Step 3: Store shortest distance of visited nodes
        dist = {}

        while minHeap:

            currDist, node = heapq.heappop(minHeap)

            # Skip if already processed
            if node in dist:
                continue

            # Record shortest distance
            dist[node] = currDist

            # Visit neighbors
            for nei, weight in graph[node]:

                # Only process unvisited nodes
                if nei not in dist:
                    heapq.heappush(minHeap, (currDist + weight, nei))

        # If not all nodes are reached
        if len(dist) != n:
            return -1

        # Maximum shortest distance
        return max(dist.values())