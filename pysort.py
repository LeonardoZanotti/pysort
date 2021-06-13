import sys
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy.random import randint

fig = plt.figure(figsize=(17, 10), dpi=80)

frames = 1000
x = range(100)
y = randint(0, 100, 100)
barcollection = plt.bar(x, y, 0.8)

plt.yticks([i*10 for i in range(11)])
plt.xticks([i*10 for i in range(11)])
plt.ylabel('Array value')
plt.xlabel('Array index')
text = plt.text(1, 100, 'Number of operations: 0')

# Bogo Sort
def bogoSort(i):
    # sorting..
    print()

# Bubble Sort
def bubbleSort(i):
    print()
    # sorting..

# Bucket Sort
def bucketSort(i):
    print()
    # sorting..

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
def quickSort(A, start, end):
    if start >= end:
        return

    pivot = A[end]
    tovip = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, tovip)
            tovip += 1
        yield A
    swap(A, end, tovip)
    yield A

    yield from quickSort(A, start, tovip - 1)
    yield from quickSort(A, tovip + 1, end)

def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]

operations = 0
def animate(values, rects):
    global operations
    for rect, value in zip(rects, values):
        rect.set_height(value)
    operations += 1
    text.set_text('Number of operations: {}'.format(operations))

def main():
    args = sys.argv
    if (len(args) > 1):
        if (args[1] == 'bogo'):
            plt.title('Bogo sort')
            generator = bogoSort
        elif (args[1] == 'bubble'):
            plt.title('Bubble sort')
            generator = bubbleSort
        elif (args[1] == 'bucket'):
            plt.title('Bucket sort')
            generator = bucketSort
        elif (args[1] == 'heap'):
            plt.title('Heap sort')
            generator = heapSort
        elif (args[1] == 'insertion'):
            plt.title('Insertion sort')
            generator = insertionSort
        elif (args[1] == 'merge'):
            plt.title('Merge sort')
            generator = mergeSort
        elif (args[1] == 'radix'):
            plt.title('Radix sort')
            generator = radixSort
        elif (args[1] == 'selection'):
            plt.title('Selection sort')
            generator = selectionSort
        elif (args[1] == 'smooth'):
            plt.title('Smotth sort')
            generator = smoothSort
        elif (args[1] == 'quick'):
            plt.title('Quick sort')
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
    plt.show()

if __name__ == '__main__':
    main()
