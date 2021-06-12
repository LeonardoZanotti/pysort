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
    """In-place bubble sort."""

    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A

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
    """In-place insertion sort."""

    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            j -= 1
            yield A

# Merge Sort
def mergeSort(A, start, end):
    """Merge sort."""
    if (end <= start):
        return
    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A

def merge(A, start, mid, end):
    """Helper function for merge sort."""
    
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A

# Radix Sort
def radixSort(i):
    print()
    # sorting..

# Selection Sort
def selectionSort(i):
    """In-place selection sort."""
    if len(A) == 1:
        return

    for i in range(len(A)):
        # Find minimum unsorted value.
        minVal = A[i]
        minIdx = i
        for j in range(i, len(A)):
            if A[j] < minVal:
                minVal = A[j]
                minIdx = j
            yield A
        swap(A, i, minIdx)
        yield A


# Smooth Sort
def smoothSort(i):
    print()
    # sorting..

# Quick Sort
def quickSort(A, start, end):
    """In-place quicksort."""

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quickSort(A, start, pivotIdx - 1)
    yield from quickSort(A, pivotIdx + 1, end)

def swap(A, i, j):
    """Helper function to swap elements i and j of list A."""

    if i != j:
        A[i], A[j] = A[j], A[i]

operations = 0
def animate(A, rects):
    global operations
    print(A, rects)
    # for a, b in enumerate(barcollection):
        # b.set_height(y[a])
    for rect, val in zip(rects, A):
        rect.set_height(val)
    operations += 1
    print(operations)
    text.set_text('Number of operations: {}'.format(operations))

    # text.set_text("# of operations: {}".format(operations))

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
