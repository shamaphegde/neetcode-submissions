class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        # t=set(nums)
        # t=list(t)
        # i=0
        # count=0
        # for i in range(len(t)):
        #     if t[i]-t[i-1]==1 and t[i+1]-t[i]==1:
        #         count+=1
        # return count
        nset=set(nums)
        lon=0
        for n in nums:
            if (n-1) not in nset:
                len=0
                while((n+len)) in nset:
                    len+=1
                lon= max(len, lon)
        return lon


