class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_indices = dict()
        for i in range(len(nums)):
            array_indices[nums[i]] = i
        
        for i in range(len(nums)):
            need = target - nums[i]
            
            possible_index = array_indices.get(need, None)
            if possible_index is not None and possible_index != i:
                ans = sorted([i, possible_index])
                return ans