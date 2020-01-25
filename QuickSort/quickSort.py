# Merge Sort Algorithm
# Calculate the number of inversions in the file
import random

def filetoArray(file):
    file = open(file, 'r')
    IntegerArray = []
    for line in file.readlines():
        IntegerArray.append(int(line.replace('\n','')))
    return IntegerArray

def partitionAlgo(arrayToSort, j, start, end):
     if end >= start:
         i = start
         while i <= end:
             if i > j and arrayToSort[i] < arrayToSort[j]:
                 arrayToSort.insert(j, arrayToSort.pop(i))
                 j = j + 1
                 i = i + 1
             elif i < j and arrayToSort[i] > arrayToSort[j]:
                 arrayToSort.insert(j, arrayToSort.pop(i))
                 j = j - 1
             else:
                i = i+1
     return j

def split(start, end):
    return random.randint(start,end)

# this function sorts the array according to the merge sort algorithm
def quickSort(arrayToSort, start, end):
     if start < end:
         j = split(start, end)
         j = partitionAlgo(arrayToSort, j, start, end)
         quickSort(arrayToSort, start, j-1)
         quickSort(arrayToSort, j+1, end)
     else:
        return


if __name__ == "__main__":
    IntegerArray = filetoArray("IntegerArray.txt")
    #IntegerArray = [1,4,5,3,2]
    n = len(IntegerArray)
    quickSort(IntegerArray, 0 , n -1)
    print IntegerArray
