# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if len(nums)==1:
#             if nums[0]==target:
#                 return 0
#             else:
#                 return -1
#         l,r=0,len(nums)-1
#         while l<r:
#             k=l+(r-l)//2
#             if nums[k]==target:
#                 return k
#             elif nums[k]>target and nums[k]>nums[r]:
#                 l=k
#             elif nums[k]<target and nums[k]>nums[r]:
#                 r=k
#             else:
#                 return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
