# problem : find the peak valley in the array (meaning the value is greater than both left and right side 
#           value and both sides of the index outside the array is consider -inf)

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        mid = 0
        
        while end >= start:
            
            mid = (start+end) // 2
            
            inclineL = False
            declineR = False
            
            if(mid-1 < 0 or nums[mid] > nums[mid-1]):
                inclineL = True
            if(mid+1 > len(nums)-1 or nums[mid] > nums[mid+1]):
                declineR = True
            
            mid = ( start + end ) // 2
            
            if(inclineL and declineR):
                return mid
            elif(inclineL):
                start = mid+1
            else:
                end = mid-1
        
        return mid