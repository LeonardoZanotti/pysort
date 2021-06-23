import sys
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy.random import randint
import numpy as np
from time import sleep
import random

fig = plt.figure(figsize=(17, 10), dpi=80)

x = range(100)
# y = list(range(100))
# random.shuffle(y)
y = randint(0, 100, 100)
barcollection = plt.bar(x, y, 0.8)

plt.yticks([i*10 for i in range(11)])
plt.xticks([i*10 for i in range(11)])
plt.ylabel('Array value')
plt.xlabel('Array index')
text = plt.text(1, 100, 'Number of operations: 0')

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
def bucketSort(arr, buckets):
    bucketsArr = []
    standardArr = []
    standard = int(len(arr)/buckets) + 1

    for i in range(standard):
        standardArr.append(standard * i)

    for i in range(standard - 1):
        bucketsArr.append([])
        for j in range(len(arr)):
            if (arr[j] >= standardArr[i] and arr[j] < standardArr[i + 1]):
                bucketsArr[i].append(arr[j])
    # yield from quickSort(bucketsArr[i], 0, len(bucketsArr[i]) - 1)

    index = 0
    a = 0
    for i in range(buckets):
        a += len(bucketsArr[i])
        print(a)
        for j in range(len(bucketsArr[i])):
            arr[index] = bucketsArr[i][j]    
            index += 1
            yield arr

    yield arr
    

# Heap Sort
def heapSort(i):
    print()
    # sorting..

# Insertion Sort
def insertionSort(i):
    print()
    # sorting..

# Merge Sort
def mergeSort(i):
    print()
    # sorting..

# Radix Sort
def radixSort(i):
    print()
    # sorting..

# Selection Sort
def selectionSort(i):
    print()
    # sorting..

# Smooth Sort
def smoothSort(i):
    print()
    # sorting..

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

operations = 0
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
            generator = bucketSort(y, 10)
        elif (args[1] == 'heap'):
            title = 'Heap sort'
            generator = heapSort
        elif (args[1] == 'insertion'):
            title = 'Insertion sort'
            generator = insertionSort
        elif (args[1] == 'merge'):
            title = 'Merge sort'
            generator = mergeSort
        elif (args[1] == 'radix'):
            title = 'Radix sort'
            generator = radixSort
        elif (args[1] == 'selection'):
            title = 'Selection sort'
            generator = selectionSort
        elif (args[1] == 'smooth'):
            title = 'Smotth sort'
            generator = smoothSort
        elif (args[1] == 'quick'):
            title = 'Quick sort'
            generator = quickSort(y, 0, 99)
        else:
            print('(!) -- Error - invalid sorting method - choose one: bogo, bubble, bucket, heap, insertion, merge, radix, selection, smooth, quick')
            exit(0)
    else:
        print('(!) -- Error - invalid sorting method - choose one: bogo, bubble, bucket, heap, insertion, merge, radix, selection, smooth, quick')
        exit(0)

    anim = animation.FuncAnimation(
        fig,
        animate,
        repeat=False,
        fargs=(barcollection, ),
        blit=False,
        frames=generator,
        interval=10
    )
    plt.title(title)

    if (save):
        print('Saving gif...')
        writergif = animation.PillowWriter(fps=30)
        anim.save('{}.gif'.format(title), writer=writergif)
    else:
        plt.show()

if __name__ == '__main__':
    main()
