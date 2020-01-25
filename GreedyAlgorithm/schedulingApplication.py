class GreedyAlgorithm(object):
      def __init__(self):
          self.jobsOrder = []

      def readFromFile(self, file):
          file = open(file, 'r')
          i = 0
          lines = file.read().splitlines()
          for line in lines:
              if i !=0:
                  self.addJob(line, i)
              i += 1

          #print self.jobsOrder

      def addJob(self, line, i):
          el = line.split(" ")
          sort = float(el[0])/float(el[1])
          self.jobsOrder.append([i, el[0], el[1], sort])


      def sortJobs(self):
          return(sorted(self.jobsOrder, key = lambda x: x[3], reverse = True))

if __name__ == "__main__":
    jobSorter = GreedyAlgorithm()
    jobSorter.readFromFile("jobs.txt")
    jobSorter.sortJobs()
