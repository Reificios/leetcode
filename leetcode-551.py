# problem : a student can either "A" absent, "L" late, "P" present given in a form of string
#           if a student absent 2 or more times total, the student fail
#           if a student late 3 or more consecutive times, the student fail
#           return false if fail, else return true

# solution : straight forward

def checkRecord(self, s: str) -> bool:
    curConsecLate = 0
    lastLate = False
    absent = 0
    for i in s:
        if i == 'A':
            absent += 1
            if absent >= 2:
                return False
        if i == "L":
            curConsecLate += 1
            lastLate = True
            if(curConsecLate >= 3):
                return False
        else:
            lastLate = False
            curConsecLate = 0
    return True