class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=set()
        for i in numbers:
            a.add(i)
            if target-i in a:
                b=numbers.index(i)
                c=numbers.index(target-i)
                if i> target-i:
                    
                    g=[c+1,b+1]
                else:
                    g=[b+1,c+1]
            a.add(i)
        return g