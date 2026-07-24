class Solution:
    def isValid(self, s: str) -> bool:
        # Micro-optimization 1: Quick fail for odd lengths (pairs are impossible)
        if len(s) % 2 != 0:
            return False
            
        stack = []
        # Mapping closing brackets to their matching open brackets
        b = {")": "(", "]": "[", "}": "{"}
        
        for c in s:
            if c in b:
                # Micro-optimization 2: pop() with a default value to avoid double lookup
                # If stack is empty, pop() fails, so we simulate an invalid character using None
                if not stack or stack.pop() != b[c]:
                    return False
            else:
                stack.append(c)
                
        # Micro-optimization 3: 'not stack' directly returns a boolean
        return not stack