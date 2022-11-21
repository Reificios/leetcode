# class KthLargest:

#     def __init__(self, k: int, nums: list):
#         self.k = k
#         self.nums = sorted(nums)

#     def add(self, val: int) -> int:
#         if len(self.nums) == 0:
#             self.nums.append(val)
#             return self.nums[-self.k]
#         start = 0
#         end = len(self.nums)-1
#         mid = 0
#         while start < end:
#             mid = (start+end) // 2
#             if(self.nums[mid] == val):
#                 start = mid
#                 break
#             elif(self.nums[mid] < val):
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         if(self.nums[start] <= val):
#             self.nums.insert(start+1, val)
#         else:
#             self.nums.insert(start, val)
#         print(self.nums)
#         return self.nums[-self.k]

# test = KthLargest(7,[-10,1,3,1,4,10,3,9,4,5,1])
# added = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,10,11,5,6,2,4,7,8,5,6,2,4,7,8,5,6]
# while(added):
#     test.add(added[0])
#     added.pop(0)

# # [-4 -3 -2 0]

class KthLargest:

    def __init__(self, k: int, nums: list):
        self.k = k
        self.nums = sorted(nums)[-k:]

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
        if(len(self.nums) < self.k or val > self.nums[0]):
            if(len(self.nums) >= self.k):
                self.nums.pop(0)
            start = 0
            end = len(self.nums)-1
            mid = 0
            while start < end:
                mid = (start+end) // 2
                if(self.nums[mid] == val):
                    start = mid
                    break
                elif(self.nums[mid] < val):
                    start = mid + 1
                else:
                    end = mid - 1
            if(not self.nums or self.nums[start] > val):
                self.nums.insert(start, val)
            else:
                self.nums.insert(start+1, val)
        return self.nums[0]

    def printd(self):
        print(self.nums)

test = KthLargest(2,[0])
added = [-1,1,-2,-4,3]
while(added):
    print(test.add(added[0]))
    test.printd()
    added.pop(0)