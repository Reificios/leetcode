# problem : given 2 sorted array, one size n, the other size m, find the median of both combined
#          

# Solution :
#       1. Median of combined list = (n+m)//2 
#       2. Create pointer for the first entry of both array
#       3. Move the one with lower value / either one of equal until moved for the value calculated in stage 1
#       4. If (n+m)%2 == 0, med = average of 2 value, else the higher one
# 
#       If any list are exausted first, keep track and move the other one instead

def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    exausted = 0 # if 1 list 1 exausted, if 2 list 2 exausted
    if(not nums1):
        exausted = 1
    elif(not nums2):
        exausted = 2
    len1 = len(nums1)
    len2 = len(nums2)
    pointer1 = 0
    pointer2 = 0
    mid = (len1 + len2) // 2
    totalOdd = True if (len1 + len2) % 2 != 0 else False
    if not totalOdd:
        mid -= 1
    start = 0

    while start != mid:
        if(exausted == 0):
            if(nums1[pointer1] <= nums2[pointer2]):
                pointer1 += 1
                if pointer1 == len1:
                    exausted = 1
            else:
                pointer2 += 1
                if pointer2 == len2:
                    exausted = 2
        elif(exausted == 1):
            pointer2 += 1
        else:
            pointer1 += 1
        start += 1
    # print(f'exausted = {exausted}, totalOdd = {totalOdd}')
    # print(pointer1, pointer2, nums1[pointer1], nums2[pointer2])
    if(totalOdd):
        if(exausted == 0):
            return nums1[pointer1] if nums1[pointer1] < nums2[pointer2] else nums2[pointer2]
        elif(exausted == 1):
            return nums2[pointer2]
        return nums1[pointer1]
    else:
        if(exausted == 0):
            if(nums1[pointer1] <= nums2[pointer2]):
                if(pointer1+1 == len1 or nums1[pointer1+1] > nums2[pointer2]):
                    return (nums1[pointer1] + nums2[pointer2])/2
                else:
                    return (nums1[pointer1] + nums1[pointer1+1])/2
            else:
                if(pointer2+1 == len2 or nums2[pointer2+1] > nums1[pointer1]):
                    return (nums1[pointer1] + nums2[pointer2])/2
                else:
                    return (nums2[pointer2] + nums2[pointer2+1])/2
        elif(exausted == 1):
            return (nums2[pointer2] + nums2[pointer2+1])/2
        return (nums1[pointer1] + nums1[pointer1+1])/2

array1 = [1,2]
array2 = [3,4]
print(findMedianSortedArrays(array1,array2))