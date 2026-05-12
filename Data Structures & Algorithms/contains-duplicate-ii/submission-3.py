class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0
        
        for right in range(len(nums)):
            # 1. Check if the current number is already in our window
            if nums[right] in window:
                return True
            
            # 2. Add the current number to the set
            window.add(nums[right])
            
            # 3. If the window size exceeds k, remove the oldest element
            if len(window) > k:
                window.remove(nums[left])
                left += 1
                
        return False