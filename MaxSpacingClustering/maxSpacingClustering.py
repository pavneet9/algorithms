
graph = []
rankNodes = {}             # collection of number of nodes in a cluster
parentNodes = {}           # parent node of a particular cluster
total_clusters = 0
index = 0

fileName = "clustering1.txt"

file = open(fileName, r)

for f in file:
    if(total_clusters == 0):
        num_clusters = int(f.strip())
    else:
        node1, node2, edge_cost = map(int, f.split())
        graph.append([node1, node2, edge_cost])

graph = sorted(graph, key=lambda x: x[2])

def increaseRank(parentNode, rank):
    for key in parentNodes.keys():
        if parentNodes[parentNode] == parentNode:
           rankNodes[parentNode] == rank

def changeLeader(oldLeader, newLeader):
    for key in parentNodes.keys():
        if parentNodes[parentNode] == oldLeader:
           parentNodes[parentNode] == newLeader

while total_clusters < 4:
        if graph[index][0] in rankNodes:
           if graph[index][1] not in rankNodes:
                 parentNodes[graph[index][1]] = parentNodes[graph[index][0]]
                 increaseRank(parentNodes[graph[index][0]], rankNodes[graph[index][0]] + 1)
                 total_clusters -= 1
        else:
           if graph[index][1] in rankNodes:
                 parentNodes[graph[index][0]] = parentNodes[graph[index][1]]
                 increaseRank(parentNodes[graph[index][1]], rankNodes[graph[index][1]] + 1)
                 total_clusters -= 1
           else:
                 parentNodes[graph[index][0]] = graph[index][0]
                 parentNodes[graph[index][1]] = graph[index][0]
                 rankNodes[graph[index][0]] = 2
                 rankNodes[graph[index][1]] = 2
                 total_clusters -= 1

      if graph[index][0] in rankNodes:
         if graph[index][1] in rankNodes:
             if parentNodes[graph[index][0]] != parentNodes[graph[index][1]]:
                # merge two clusters with each other
                rank0 = rankNodes[graph[index][0]]
                rank1 = rankNodes[graph[index][1]]
                if rank0 > rank1:
                    newRank = rankNodes[graph[index][0]] + rankNodes[graph[index][1]]
                    changeLeader(graph[index][0], graph[index][1])
                    increaseRank(parentNodes[graph[index][0]], newRank)
                else:
                    newRank = rankNodes[graph[index][0]] + rankNodes[graph[index][1]]
                    changeLeader(graph[index][1], graph[index][0])
                    increaseRank(parentNodes[graph[index][1]], newRank)

      index += 1
