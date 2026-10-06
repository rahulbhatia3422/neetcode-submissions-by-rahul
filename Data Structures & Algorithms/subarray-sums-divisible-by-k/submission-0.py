class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        result = 0

        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for num in nums:

            prefix_sum += num
            remain = prefix_sum % k


            result += prefix_cnt[remain]

            prefix_cnt[remain] += 1

        return result
        