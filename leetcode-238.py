# problem : given an array nums, return an array answer such that answer[i] is equal to the product of all 
#           the elements of nums except nums[i] without using division operation within O(n) time
# follow-up : answer in O(1) extra spave (answer doesn't count)

# def productExceptSelf(nums: list) -> list:
#     length = len(nums)
#     prefixProd = []
#     suffixProd = []
#     output = []
    
#     for i in range(length):
#         if i == 0:
#             prefixProd.append(1)
#             suffixProd.append(1)
#         else:
#             prefixProd.append(nums[i-1] * prefixProd[i-1])
#             suffixProd.append(nums[length-i] * suffixProd[i-1])
        
#     for i in range(length):
#         output.append(prefixProd[i] * suffixProd[length-i-1])
        
#     return output

def productExceptSelf(nums: list) -> list:
    length = len(nums)
    suffix = 1
    output = []
    
    for i in range(length):
        if i == 0:
            output.append(1)
        else:
            output.append(nums[i-1] * output[i-1])
        
    for i in range(length):
        output[length-i] = output[length-i] * suffix
        suffix *= nums[length-i]
        
    return output