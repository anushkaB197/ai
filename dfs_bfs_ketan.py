# BFS Algorithm
adj = {1: [2, 3], 2: [1], 3: [1, 4], 4: [3]}


def BFS(adj, startnode, numofnodes):
    v = [0]*(numofnodes+1)
    que = []
    v[startnode] = 1
    que.append(startnode)

    while (len(que) != 0):
        adjele = que.pop(0)
        print(adjele, end=" ")
        getlist = adj.get(adjele)

        for i in getlist:
            if (v[i] == 0):
                v[i] = 1
                que.append(i)


BFS(adj, 3, 4)

# DFS Algorithm
adj = {1: [2, 3], 2: [1, 5], 3: [1, 4], 4: [3], 5: [2]}
visi = [0]*(6)

def DFS(adj, startnode):
    visi[startnode] = 1
    print(startnode, end=" ")
    for i in adj.get(startnode):
        if (visi[i] == 0):
            DFS(adj, i) #calling fun recursively

print()
DFS(adj, 1)