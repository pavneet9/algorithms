import random

def filetoAdjList(file):
    file = open(file, 'r')
    adjList = {}
    for line in file.readlines():
        vertices = line.replace("\n", "").split("	")
        adjList[vertices[0]] =  vertices[1:-1]
    return adjList

def minCuts(adjList):
    while len(adjList) > 2:
        randVert1 = random.choice(list(adjList.keys()))
        randVert2 = random.choice(adjList[randVert1])
        adjList = merge(randVert1, randVert2, adjList)
    return len(adjList[list(adjList.keys())[0]])
# takes two nodes and changes the adjlist according and replaces them with a common node
def merge(randVert1, randVert2, adjList):
    # put all the elements of list 2 in list 1
    for vertex in adjList[randVert2]:
        if vertex !=  randVert1:
            adjList[randVert1].append(vertex)
        adjList[vertex].remove(randVert2)
        #print adjList[vertex]
        if vertex !=  randVert1:
            adjList[vertex].append(randVert1)
    adjList.pop(randVert2)
    return adjList

if __name__ == "__main__":
    adjList = filetoAdjList("kargerMinCut.txt")
    #IntegerArray = [1,4,5,3,2]
    lenMinCuts = minCuts(adjList)
    print lenMinCuts
