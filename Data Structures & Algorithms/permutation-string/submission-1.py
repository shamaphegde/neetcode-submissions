class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        # Step 1: Initialize frequency arrays for s1 and the first window of s2
        s1Count = [0] * 26
        s2Count = [0] * 26
        
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
            
        # Step 2: Slide the window across s2
        for i in range(len(s1), len(s2)):
            if s1Count == s2Count:
                return True
                
            # Add the new character entering the window from the right
            s2Count[ord(s2[i]) - ord('a')] += 1
            # Remove the old character leaving the window from the left
            s2Count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
        # Check the very last window position
        return s1Count == s2Count