from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # 1. Forward pass for prefixes
        prefix = 1
        for i in range(n):
            result[i] = prefix      # First, store the running product (excludes nums[i])
            prefix *= nums[i]       # Then, update it for the NEXT element
        
        # 2. Backward pass for postfixes
        postfix = 1
        for i in range(n - 1, -1, -1): # Start from the last index, move to 0
            result[i] *= postfix    # Multiply the existing prefix by the postfix
            postfix *= nums[i]      # Update postfix for the NEXT element to the left
            
        return result