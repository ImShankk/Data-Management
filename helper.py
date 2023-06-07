# Helper function
#ALLOWS ME TO USE THE SORTS AND ALGORITHMS MUCH EASIER BY JUST USING THE FUNCTION

#SORTING ALGORITHMS

#INSERTION SORT
def insertionSort(anArray):
  for n in range(1, len(anArray)):
    insertion = anArray[n]
    i = n - 1
    while i >= 0 and anArray[i] > insertion:
      anArray[i + 1] = anArray[i]
      i -= 1
    anArray[i + 1] = insertion


#BUBBLE SORT
def bubbleSort(anArray):
  for n in range(len(anArray) - 1):
    for i in range(len(anArray) - n - 1):
      if anArray[i] > anArray[i + 1]:
        anArray[i], anArray[i + 1] = anArray[i + 1], anArray[i]


#SELECTION SORT
def selectionSort(anArray):
  for n in range(len(anArray) - 1):
    min = n
    for i in range(n + 1, len(anArray)):
      if anArray[i] < anArray[min]:
        min = i
    anArray[n], anArray[min] = anArray[min], anArray[n]

#SEARCHING ALGORITHMS

#Binary Search
def binarySearch(anArray, item):
  #2 indexes other than middle
  lowIndex = 0
  highIndex = len(anArray) - 1

  #find average for low index
  while lowIndex <= highIndex:
    averageIndex = (lowIndex + highIndex) / 2
    middleIndex = int(round(averageIndex, 2))

    if item == anArray[middleIndex]:
      return middleIndex
    elif item < anArray[middleIndex]:
      highIndex =  (-1 + middleIndex)
    else:
      lowIndex = (1 + middleIndex)

  return -1


#Linear Search
def linearSearch(anArray, item):
  for n in range (len(anArray)):
    if anArray[n] == item:
        return n
  return -1

#Binary Search number 2 found on internet
def diffBinary(list, key, value):
  low = 0
  max = len(list) - 1
  while low <= max:
    mid = (low + max) // 2
    if list[mid][key] == value:
      return mid
    elif list[mid][key] < value:
      low = mid + 1
    else:
      max = mid - 1
  return -1

#BUBBLE SORT BUT 2 PARAMRTERS found on internet after research
def bubbleSortTwo(anArray, key):
  for n in range(len(anArray)):
    #include the second one
    for i in range(n+1, len(anArray)):
      #check for the higher value
      if anArray[n][key] > anArray[i][key]:
        #swap value if higher
        anArray[n], anArray[i] = anArray[i], anArray[n]