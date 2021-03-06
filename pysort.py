import sys
import os
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy.random import randint
import numpy as np
from time import sleep
import random
from math import ceil

fig = plt.figure(figsize=(17, 10), dpi=80)

numOfElements = 100
numOfElementsByTen = numOfElements / 10
operations = 0
x = range(numOfElements)
# y = list(range(numOfElements))
# random.shuffle(y)
y = randint(0, numOfElements, numOfElements)
barcollection = plt.bar(x, y, 0.8)

plt.yticks([i * numOfElementsByTen for i in range(11)])
plt.xticks([i * numOfElementsByTen for i in range(11)])
plt.ylabel('Array value')
plt.xlabel('Array index')
text = plt.text(1, numOfElements, 'Number of operations: 0')

# Bogo Sort
def bogoSort(arr):
    # Stupid sort
    # while not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
    #     random.shuffle(arr)
    #     yield arr
    # yield arr

    # Less stupid sort
    global y
    if (len(arr) > 1):
        for perm in bogoSort(arr[1:]):
            if (len(y) == len(x) and all(y[j] <= y[j + 1] for j in range(len(y) - 1))):
                break
            for i in range(len(perm) + 1):
                y = list(perm[:i]) + [arr[0]] + list(perm[i:])
                yield y
                if (len(y) == len(x) and all(y[j] <= y[j + 1] for j in range(len(y) - 1))):
                    break
        yield y
    else:
        yield list(arr)

# Bubble Sort
def bubbleSort(arr):
    while not (all(y[j] <= y[j + 1] for j in range(len(y) - 1))):
        for i in range(len(arr) - 1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            yield arr


# Bucket Sort
# Doesn't work with numOfElements not divisible by 10
def bucketSort(arr, buckets):
    bucketsArr = []

    for i in range(buckets):
        bucketsArr.append([])
        for j in range(len(arr)):
            if (arr[j] >= 10 * i and arr[j] < 10 * (i + 1)):
                bucketsArr[i].append(arr[j])
        yield from quickSort(bucketsArr[i], 0, len(bucketsArr[i]) - 1)

    index = 0
    for i in range(buckets):
        for j in range(len(bucketsArr[i])):
            arr[index] = bucketsArr[i][j]    
            index += 1
            yield arr

    yield arr
    

# Heap Sort
def heapSort(arr):
    maxValue = -1
    arrayIndexes = []
    for i in range(len(arr)):
        arrayIndexes.append(i)
        if (arr[i] >= maxValue):
            maxValue, maxValueIndex = arr[i], i

    if (not "maxValueIndex" in locals()):
        return

    arr[len(arr) - 1], arr[maxValueIndex] = arr[maxValueIndex], arr[len(arr) - 1]
    yield arr

    for i in range(len(arr) - 1, -1, -1):
        if ((ceil(i / 2) - 1) in arrayIndexes and arr[(ceil(i / 2) - 1)] > arr[i]):
            arr[(ceil(i / 2) - 1)], arr[i] = arr[i], arr[(ceil(i / 2) - 1)]
        yield arr

    yield from heapSort(arr[:len(arr) - 1])

# Insertion Sort
def insertionSort(arrSorted, arr, index):
    if (index < numOfElements):
        arrSorted.append(arr[index])
        if (index != 0):
            indexCopy = index
            for i in range(len(arrSorted) - 2, -1, -1):
                if (arrSorted[indexCopy] < arrSorted[i]):
                    arrSorted[indexCopy], arrSorted[i] = arrSorted[i], arrSorted[indexCopy]
                    indexCopy -= 1
                    yield arrSorted
                else:
                    break

        yield from insertionSort(arrSorted, arr, index + 1)

# Merge Sort
def mergeSort(arr):
    arrOfArrs = []

    for i in range(len(arr)):
        arrOfArrs.append([arr[i]])

    yield arr

    while (len(arrOfArrs) != 1):
        arrOfArrsCopy = []

        for i in range(len(arrOfArrs) - 1):
            if (i % 2 == 0):
                sortedArr = []
                indexesArrayI = []
                indexesArrayI1 = []

                for j in range(len(arrOfArrs[i] + arrOfArrs[i + 1])):
                    sortedArr.append(numOfElements + 1)

                    for k in range(len(arrOfArrs[i])):
                        if (sortedArr[j] > arrOfArrs[i][k] and k not in indexesArrayI):
                            sortedArr[j] = arrOfArrs[i][k]
                            index = i
                            kindex = k
        
                    for k in range(len(arrOfArrs[i + 1])):
                        if (sortedArr[j] > arrOfArrs[i + 1][k] and k not in indexesArrayI1):
                            sortedArr[j] = arrOfArrs[i + 1][k]
                            index = i + 1
                            kindex = k

                    indexesArrayI.append(kindex) if (index == i) else indexesArrayI1.append(kindex)

                arrOfArrsCopy.append(sortedArr)
            
            if ((i == len(arrOfArrs) - 2) and (i % 2 == 1)):
                sortedArr = []
                indexesArrayI = []
                indexesArrayI1 = []

                for j in range(len(arrOfArrsCopy[len(arrOfArrsCopy) - 1] + arrOfArrs[i + 1])):
                    sortedArr.append(numOfElements + 1)

                    for k in range(len(arrOfArrsCopy[len(arrOfArrsCopy) - 1])):
                        if (sortedArr[j] > arrOfArrsCopy[len(arrOfArrsCopy) - 1][k] and k not in indexesArrayI):
                            sortedArr[j] = arrOfArrsCopy[len(arrOfArrsCopy) - 1][k]
                            index = i
                            kindex = k
                
                    for k in range(len(arrOfArrs[i + 1])):
                        if (sortedArr[j] > arrOfArrs[i + 1][k] and k not in indexesArrayI1):
                            sortedArr[j] = arrOfArrs[i + 1][k]
                            index = i + 1
                            kindex = k

                    indexesArrayI.append(kindex) if (index == i) else indexesArrayI1.append(kindex)
                
                arrOfArrsCopy[len(arrOfArrsCopy) - 1] = sortedArr

            yield [item for sublist in arrOfArrsCopy for item in sublist]

        arrOfArrs = arrOfArrsCopy

# Radix Sort
def radixSort(arr, maxValue, index):
    if (index <= maxValue):
        arrDecimals = np.zeros((10,), dtype = int)
        arrChar = arr.copy()
        newArr = arr.copy()

        ## couting sort starts
        for i in range(len(arr)):
            arrChar[i] = int((str(arr[i]).zfill(maxValue))[maxValue - index])
            arrDecimals[arrChar[i]] += 1

        for j in range(1, len(arrDecimals)):
            arrDecimals[j] = arrDecimals[j] + arrDecimals[j - 1]
        
        for k in range(len(arr) - 1, -1, -1):
            newArr[arrDecimals[arrChar[k]] - 1] = arr[k]
            arrDecimals[arrChar[k]] -= 1
            yield newArr
        ## couting sort ends

        yield from radixSort(newArr, maxValue, index + 1)

# Selection Sort
def selectionSort(arr, arrSorted):
    global numOfElements
    arrCopy = arr.copy()
    arrSortedCopy = arrSorted.copy()
    minValue = numOfElements + 1
    for i in range(len(arr)):
        if (arrCopy[i] < minValue):
            minValue = arr[i]
            minValueIndex = i
    if ("minValueIndex" in locals()):
        arrSortedCopy.append(minValue)
        arrCopy = np.delete(arrCopy, minValueIndex)
    yield arrSortedCopy
    yield from selectionSort(arrCopy, arrSortedCopy)

# Quick Sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        yield arr
    if low < high:
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        mid = i + 1
        arr[mid], arr[high] = arr[high], arr[mid]
        yield arr
        yield from quickSort(arr, low, mid - 1)
        yield from quickSort(arr, mid + 1, high)

def animate(values, rects):
    global operations
    for rect, value in zip(rects, values):
        rect.set_height(value)
    operations += 1
    text.set_text('Number of operations: {}'.format(operations))

def main():
    args = sys.argv
    save = False
    if (len(args) > 1):
        if (len(args) > 2 and args[2] == 'save'):
            save = True
        if (args[1] == 'bogo'):
            title = 'Bogo sort'
            generator = bogoSort(y)
        elif (args[1] == 'bubble'):
            title = 'Bubble sort'
            generator = bubbleSort(y)
        elif (args[1] == 'bucket'):
            title = 'Bucket sort'
            generator = bucketSort(y, int(numOfElementsByTen))
        elif (args[1] == 'heap'):
            title = 'Heap sort'
            generator = heapSort(y)
        elif (args[1] == 'insertion'):
            title = 'Insertion sort'
            generator = insertionSort([], y, 0)
        elif (args[1] == 'merge'):
            title = 'Merge sort'
            generator = mergeSort(y)
        elif (args[1] == 'radix'):
            title = 'Radix sort'
            generator = radixSort(y, len(str(max(y))), 1)
        elif (args[1] == 'selection'):
            title = 'Selection sort'
            generator = selectionSort(y, [])
        elif (args[1] == 'quick'):
            title = 'Quick sort'
            generator = quickSort(y, 0, numOfElements - 1)
        else:
            print('(!) -- Error - invalid sorting method - choose one: bogo, bubble, bucket, heap, insertion, merge, radix, selection, quick')
            exit(0)
    else:
        print('(!) -- Error - invalid sorting method - choose one: bogo, bubble, bucket, heap, insertion, merge, radix, selection, quick')
        exit(0)

    anim = animation.FuncAnimation(
        fig,
        animate,
        repeat=False,
        fargs=(barcollection, ),
        blit=False,
        frames=generator,
        interval=10,
        save_count=300
    )
    plt.title(title)

    if (save):
        print('Saving gif...')
        writergif = animation.PillowWriter(fps=30)
        if (not os.path.isdir('./gifs')):
            os.makedirs('./gifs')
        anim.save('./gifs/{}.gif'.format(title), writer=writergif)
    else:
        plt.show()

if __name__ == '__main__':
    main()
