from collections import defaultdict
import random
import sys

sys.setrecursionlimit(10**6)

class GraphScc(object):
     def __init__(self):
        self.graph = defaultdict(list)
        self.graphT = defaultdict(list)
        self.FinishingTime = {}
        self.time = 1
        self.leader = []

     def readFromFile(self, file):
        file = open(file, 'r')
        for line in file.readlines():
            el = line.split(" ")
            self.addEdge(el[1], el[0],True)             # From the file we load an already transposed matrix
            self.addEdge(el[0], el[1],False)

     def addEdge(self, base, next, transpose = False):
          if transpose == True:
              self.graphT[base].append(next)
          else:
              self.graph[base].append(next)

     def getFinshingTime(self):
         self.allVertices =list(self.graphT.keys())
         while self.allVertices:
             vertex = random.choice(self.allVertices)
             self.dfsUtility(vertex)

     def dfsUtility(self, vertex):
          self.allVertices.remove(vertex)
          stack = []
          for i in self.graphT[vertex]:
              if i in self.allVertices:
                  self.dfsUtility(i)
          self.addexploredNode(vertex)

     def addexploredNode(self, vertex):
        self.FinishingTime[vertex] = self.time
        self.time = self.time + 1
        print self.FinishingTime

     def getScc(self):
         self.allVertices = list(self.graph.keys())
         while self.allVertices:
             vertex = max(my_dict.keys(), key=(lambda k: my_dict[k]))
             self.addLeader(vertex)
             self.dfsUtility(vertex)

     def addLeader(self, vertex):
        self.leader.append(vertex)

     def findScc(self, vertex):
          self.allVertices.remove(vertex)
          stack = []
          for i in self.graph[vertex]:
              if i in self.allVertices:
                  self.findScc(i)

     def returnLeaders(self):
        return self.leader



# Once the Numbering is done then find SCC, and also keep checks on what has been computed till now
if __name__ == "__main__":
    scc = GraphScc()
    scc.readFromFile("SCC.txt")
    scc.getFinshingTime()
    scc.getScc()
    print scc.returnLeaders()
#    scc.getTranspose()
#    graph.getFinshingTime()












# Upload the file
