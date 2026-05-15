class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            a = numbers[left]
            b = numbers[right]

            if a+b < target:
                left+=1
            elif a+b >target:
                right-=1

            else:
                return [left + 1, right + 1]
        # we return empty list when no solution was found
        return []