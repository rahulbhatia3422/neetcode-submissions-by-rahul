class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        flat_lst = [item for sublist in grid for item in sublist]
        max_num = len(flat_lst)

        freq_map = {}
        repeated = -1
        missing = -1

        # build frequency map
        for num in flat_lst:
            freq_map[num] = freq_map.get(num, 0) + 1

        # find repeated
        for k, v in freq_map.items():
            if v > 1:
                repeated = k
                break

        # find missing
        for i in range(1, max_num + 1):
            if i not in freq_map:
                missing = i
                break

        return [repeated, missing]
