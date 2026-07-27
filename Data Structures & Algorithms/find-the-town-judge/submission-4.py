class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        i=1
        j=0
        count=0
        h=trust[0][1]
        e=0
        while j<len(trust):
        
            if trust[j][i]==h and trust[j][0]!=h:
                count+=1
                j+=1
                e+=1
            elif trust[j][i]!=h and trust[j][0]!=h:
                j+=1
                count+=1
            else:
                return -1
        if e==n-1:
            return h
        else:
            return -1
            