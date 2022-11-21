# problem : search the index of the target, if not found, return where it should be in the array instead

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = 0
        
        while(end >= start):
            mid = (start + end) // 2
            if(nums[mid] > target):
                end = mid-1
            elif(nums[mid] < target):
                start = mid+1
            else:
                start = mid
                break
        if(start > len(nums)-1 or nums[start] >= target):
            return start
        else:
            return start+1