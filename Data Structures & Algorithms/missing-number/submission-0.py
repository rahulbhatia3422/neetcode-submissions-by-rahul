class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = 0
        for i in range(len(nums)+ 1):
            summ += i

        return summ - sum(nums)

        