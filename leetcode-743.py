# problem: given a network of n nodes with time to connect nodes in times, start at k, what is the max time for it to reach everyone

# solution: djikstar with an extra step

def networkDelayTime(times: list, n: int, k: int) -> int:
    graph = [[-1 for i in range(n)] for j in range(n)]
    for i in times:
        graph[i[0]-1][i[1]-1] = i[2]
    for i in graph:
        print(i)
    dist = [600005 for i in range(n)]
    dist[k-1] = 0
    used = [False for i in range(n)]
    
    minNode = 0
    minNodeVal = 600006
    
    while False in used:
        minNode = -1
        minNodeVal = 600006
    
        for i in range(n):
            if dist[i] < minNodeVal and not used[i]:
                minNode = i
                minNodeVal = dist[i]

        # print(f"choosen {minNode}")
        
        for i in range(n):
            if(graph[minNode][i] != -1 and dist[i] > dist[minNode] + graph[minNode][i]):
                dist[i] = dist[minNode] + graph[minNode][i]

        # print(dist)
        
        used[minNode] = True

    print(dist)
    res = -1
    for i in range(n):
        if(dist[i] == 600005):
            return -1
        if(dist[i] > res):
            res = dist[i]
    return res
        
test = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
print(networkDelayTime(test, 5,5))