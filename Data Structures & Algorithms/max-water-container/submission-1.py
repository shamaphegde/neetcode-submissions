# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         res=0
#         l=0
#         r=len(heights)-1
#         while l<r:
#             area=(r-l)*min(heights[r],heights[l])
#             res=max(area,res)
#             if heights[r]>=heights[l]:
#                 l+=1
#             else:
#                 r-=1
#         return res
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
