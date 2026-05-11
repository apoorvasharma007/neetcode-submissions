class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = dict()
        for i in range(len(nums)):
            num_index_map[nums[i]] = i

        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in num_index_map.keys():
                j = num_index_map[b]
                if j!= i:
                    return [i,j]
