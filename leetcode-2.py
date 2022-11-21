from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def iterateLinkList(self):
        tmp = ListNode(val = self.val, next=self.next)
        while(tmp.next != None):
            print(tmp.val, end=" ")
            tmp = tmp.next
        print(tmp.val, end=" ")
        tmp = tmp.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        stackAnswer = []
        carryOver = 0

        while(l1.next != None):
            stack1.append(l1.val)
            l1 = l1.next
        stack1.append(l1.val)
        l1 = l1.next
            
        while(l2.next != None):
            stack2.append(l2.val)
            l2 = l2.next
        stack2.append(l2.val)
        l2 = l2.next

        while stack1 or stack2:
            if(stack1 == []):
                res = stack2[0] + carryOver
                stack2.pop(0)
            elif(stack2 == []):
                res = stack1[0] + carryOver
                stack1.pop(0)
            else:
                res = stack1[0] + stack2[0] + carryOver
                stack1.pop(0)
                stack2.pop(0)
            stackAnswer.append( int(str(res)[-1]) )
            if(res >= 10):
                carryOver = 1
            else:
                carryOver = 0
        if(carryOver == 1):
            stackAnswer.append(1)

        # answ = 1->2->3->4, stack = [4 3 2 1]

        answer = None
        while(stackAnswer):
            answer = ListNode(val=stackAnswer.pop(0), next=answer)
        return answer

def createLLfromL(inputList):
    returnList = None
    while(inputList):
        returnList = ListNode(val=inputList.pop(-1), next=returnList)
    return returnList

l1 = createLLfromL([9,9,9,9,9,9,9])
l2 = createLLfromL([9,9,9,9])
sol = Solution()
l3 = sol.addTwoNumbers(l1,l2)