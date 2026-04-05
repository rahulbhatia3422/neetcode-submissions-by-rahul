class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        freq_map = {}
        num_sort = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # sort by frequency ASC, value DESC
        sorted_num = sorted(freq_map.items(), key=lambda item: (item[1], -item[0]))

        for k, v in sorted_num:
            num_sort.extend([k] * v)

        return num_sort