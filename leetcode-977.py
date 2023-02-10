# given a non-decreasing array, return an array of the squared of each numbers in a non-ddecreasing array.

def sortedSquares(self, nums: List[int]) -> List[int]:
        lennum = len(nums)
        for i in range(lennum):
            nums[i] = abs(nums[i])
        nums.sort()
        for i in range(lennum):
            nums[i] = nums[i] * nums[i]
        return nums