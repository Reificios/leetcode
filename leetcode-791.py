# given 2 strings, order and s, sort every character in s that exists in string order just like how the string order is.

def customSortString(self, order: str, s: str) -> str:
    tmp = list(s)
    pos = []
    include = []
    for i in range(len(tmp)):
        if tmp[i] in order:
            pos.append(i)
            include.append(tmp[i])
    a = 0
    while len(pos) != 0:
        # print(tmp, pos, include)
        if order[a] in include:
            tmp[pos[0]] = order[a]
            pos.pop(0)
            include.remove(order[a])
            a -= 1
        a += 1
    return "".join(tmp)