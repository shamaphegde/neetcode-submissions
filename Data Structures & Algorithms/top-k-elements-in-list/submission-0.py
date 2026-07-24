from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies safely
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
                
        # Step 2: Sort the dictionary keys based on their values in descending order
        # sorted() returns a list of keys sorted by the lambda function
        sorted_keys = sorted(seen, key=lambda x: seen[x], reverse=True)
        
        # Step 3: Return the top k elements
        return sorted_keys[:k]