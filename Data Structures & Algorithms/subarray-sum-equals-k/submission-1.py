class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_freq = {0: 1}
        curr_sum = 0
        res = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            target = curr_sum - k
            res += prefix_sum_freq.get(target,0)
            prefix_sum_freq[curr_sum] = 1 + prefix_sum_freq.get(curr_sum, 0)
        
        return res