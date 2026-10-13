class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        repeated = -1
        missing = -1
        lst = []

        freq = {}

        for i in range(1,len(nums)+1):
            if i not in nums:
                missing = i

        for num in nums:

            freq[num] = freq.get(num,0) + 1

        for k , v in freq.items():
            if v > 1:
                repeated = k

        return [repeated,missing]

        

        