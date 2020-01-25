# Implementation of dijkstra's Shortest Paths algorithm.
from collections import defaultdict

class Heap(object):
      # feel like it should be a list of tuleps
      def __init__(self):
          self.heapList = defaultdict(list)
          self.pos = {}
          self.size = 0

      def addNewHeapElement(self, vertex, distance):
          self.heapList[self.size] = [vertex, distance]
          self.pos[vertex] =  self.size
          self.heapify(self.pos[vertex])
          self.size += 1
          return [vertex, distance]

      # This will change the placements of the nodes
      def changeNodes(self, a, b):
           t = self.heapList[a]
           self.heapList[a] = self.heapList[b]
           self.heapList[b] = t
           self.pos[self.heapList[b][0]] = b
           self.pos[self.heapList[a][0]] = a
           return

      # This will be the Implementation of the bubble up algorithm
      def heapify(self, pos):
           if (pos % 2) == 0:
               parent = pos/2 -1
           else:
               parent = (pos -1)/2
           while pos > 0 and self.heapList[pos][1] < self.heapList[parent][1] :
               # Change the heaplist around
               self.changeNodes(pos, parent)
               pos = parent
               if (pos % 2) == 0 :
                   parent = pos/2 -1
               else:
                   parent = (pos -1)/2

      def extract_min(self):
         self.changeNodes(0, self.size -1 )
         minNode = self.heapList.pop(self.size -1)
         self.size = self.size - 1
         self.pos.pop(minNode[0])
         self.bubbleDown(0)
         return minNode[0], minNode[1]

      def bubbleDown(self, pos):
          left = 2*pos + 1
          right = 2*pos + 2
          smallest = pos
          if left < self.size and self.heapList[left][1] < self.heapList[smallest][1]:
              smallest = left
              self.changeNodes(smallest, left)
              self.bubbleDown(smallest)
          elif right < self.size and self.heapList[right][1] < self.heapList[smallest][1]:
              smallest = right
              self.changeNodes(smallest, left)
              self.bubbleDown(smallest)

      def newWeights(self, vertex, weight):
          if vertex in self.pos:
              pos = self.pos[vertex]
              if self.heapList[pos][1] > weight or self.heapList[pos][1] == 100000000:
                  self.heapList[pos][1] = weight
                  self.heapify(pos)
                  return True
          else:
             return False

      def checkContains(self, v):
          if v in self.pos:
              return True
          else:
              return False


class dijkstra(object):
    def __init__(self, source):
        self.heap = Heap()
        self.distanceDic = {}
        self.graph = defaultdict(list)
        self.source = source

    def readFromFile(self, file):
        file = open(file, 'r')
        for line in file.readlines():
            self.addEdge(line)

    def addEdge(self, line):
          el = line.split("\t")
          for i in range(1, len(el)-1):
              vertex, weight = el[i].split(",")
              self.graph[int(el[0])].append([vertex, weight])

    # create a Heap
    def createHeap(self):
        for v , weight in self.graph[self.source]:
            self.heap.addNewHeapElement(int(v), weight)
            self.distanceDic[v] = weight

        for i in self.graph:
            if not self.heap.checkContains(i):
                newHeapNode = self.heap.addNewHeapElement(int(i), 100000000)
                self.distanceDic[i] = 100000000

    def findShortedDistance(self):
        while len(self.heap.heapList) > 0 :
                v, weightV =self.heap.extract_min()
                self.distanceDic[v] = weightV
                for i, weight in self.graph[v]:
                    change = self.heap.newWeights(i, int(weightV) + int(weight))
                    if change:
                        self.distanceDic[v] = int(weightV) + int(weight)
        return self.distanceDic

if __name__ == "__main__":
      sp = dijkstra(1)
      sp.readFromFile("dijkstraData.txt")
      sp.createHeap()
      sp.findShortedDistance()
