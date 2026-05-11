class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        index = 0
        for i in nums:
            ans[index]=i
            ans[index+n]=i
            index+=1
        return ans