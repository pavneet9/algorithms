# Merge Sort Algorithm
# Calculate the number of inversions in the file

def filetoArray(file):
    file = open(file, 'r')
    IntegerArray = []
    for line in file.readlines():
        IntegerArray.append(int(line.replace('\n','')))
    return IntegerArray

# this function sorts the array according to the merge sort algorithm
def mergeSort(arrayToSort):
     lenArray = len(arrayToSort)
     if(lenArray > 1):
         sortN = lenOfSubArray(lenArray)
         sub_array1 = mergeSort(arrayToSort[0:sortN])
         sub_array2 = mergeSort(arrayToSort[sortN:lenArray])
         sortedArray = []
         i = 0
         j = 0
         while (i <len(sub_array1) or j < len(sub_array2) ):
             if i == len(sub_array1):
                 sortedArray.append(sub_array2[j])
                 j = j + 1
             elif j == len(sub_array2):
                 sortedArray.append(sub_array1[i])
                 i = i + 1
             elif sub_array1[i] < sub_array2[j] :
                 sortedArray.append(sub_array1[i])
                 i = i + 1
             else:
                 sortedArray.append(sub_array2[j])
                 j = j + 1
         return sortedArray
     else:
         return arrayToSort

def lenOfSubArray(n):
     if (n % 2) == 0:
         return n/2
     else:
         return n/2 + 1
# First i need to take the file and then convert it into an array

# then i need to implement the merge sort algorith and caluclate the inversions


if __name__ == "__main__":
    IntegerArray = filetoArray("IntegerArray.txt")
    #IntegerArray = [1,4,5,3,2]
    sortedArray = mergeSort(IntegerArray)
    print sortedArray
