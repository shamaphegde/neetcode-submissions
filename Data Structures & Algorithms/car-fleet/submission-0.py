from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a = len(position)
        
        # 1. Pair up positions and speeds, then sort descending by position
        pairs = sorted(zip(position, speed), reverse=True)
        
        # 2. Calculate time to target for each car (using your list 'b')
        b = [0] * a
        for i in range(a):
            b[i] = (target - pairs[i][0]) / pairs[i][1]
            
        fleet = 0
        max_time = 0.0  # Tracks the time of the fleet leader ahead
        
        # 3. Iterate through calculated times
        for j in range(a):
            if b[j] > max_time:
                fleet += 1
                max_time = b[j]
                
        return fleet