# Knapsack Problem



class knapSackAlgorithm(object):
    def __init__(self):
        self.totalItems = 0
        self.totalWeight = 0
        self.items = []

    def readFromFiles(self, fileName):
        file = open(fileName, r)
        for f in file:
            if(self.totalItems == 0):
                self.totalWeight, self.totalItems = map(int, f.strip())
            else:
                itemValue, weight = map(int, f.split())
                self.items.append([itemValue, weight])

    def knapSackAlgorithm(self):
        for i in range(0, self.totalItems + 1):
            for j in range(0, self.totalWeight + 1):
                if i == 0 or j == 0:
                    A[i][j] = 0
                    continue
                weight = self.items[i][1]
                if j < weight:
                    A[i][j] = A[i-1][j]
                    continue
                else:
                    residual =  j - weight
                    A[i][j] = max(A[i-1][residual] + self.items[i][2], A[i-1][j] )

if __init__ =="__main__":
    knapsack = knapSackAlgorithm()
    knapsack.readFromFiles("knapsack1.txt")
    knapsack.knapSackAlgorithm()             
