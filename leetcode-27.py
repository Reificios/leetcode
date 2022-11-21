# problem : remove the val from nums, return number pof changes, nums must be changed accordingly

def removeElement(nums: list, val: int) -> int:
    total = len(nums)
    nums[:] = [i for i in nums if i != val]
    return total - len(nums)

nums = [0,1,2,2,3,0,4,2]
removeElement(nums, 2)
print(nums)