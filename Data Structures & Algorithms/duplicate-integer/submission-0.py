class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
    
        for num in nums:
        # If the number is already in our set, we found a duplicate!
            if num in seen:
                return True
        # Otherwise, add it to the set and keep moving
            seen.add(num)
        
    # If the loop finishes without finding duplicates, return False
        return False
        