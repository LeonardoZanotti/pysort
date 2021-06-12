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


def setHeights():
    for a, b in enumerate(barcollection):
        b.set_height(y[a])

# Bogo Sort
def bogoSort(i):
    # sorting..
    setHeights()

# Bubble Sort
def bogoSort(i):
    # sorting..
    setHeights()

# Bucket Sort
def bogoSort(i):
    # sorting..
    setHeights()

# Heap Sort


# Insertion Sort


# Merge Sort


# Radix Sort


# Selection Sort


# Smooth Sort


# Quick Sort

def main():
    args = sys.argv
    if (len(args) > 1):
        if (args[1] == 'bogo'):
            plt.title('Bogo sort')
            animateFunc = bogoSort
        elif (args[1] == 'bubble'):
            plt.title('Bubble sort')
            animateFunc = bubbleSort
        elif (args[1] == 'bucket'):
            plt.title('Bucket sort')
            animateFunc = bucketSort
        elif (args[1] == 'heap'):
            plt.title('Heap sort')
            animateFunc = heapSort
        elif (args[1] == 'insertion'):
            plt.title('Insertion sort')
            animateFunc = insertionSort
        elif (args[1] == 'merge'):
            plt.title('Merge sort')
            animateFunc = mergeSort
        elif (args[1] == 'radix'):
            plt.title('Radix sort')
            animateFunc = radixSort
        elif (args[1] == 'selection'):
            plt.title('Selection sort')
            animateFunc = selectionSort
        elif (args[1] == 'smooth'):
            plt.title('Smotth sort')
            animateFunc = smoothSort
        elif (args[1] == 'quick'):
            plt.title('Quick sort')
            animateFunc = quickSort
        else:
            print('(!) -- Error - invalid sorting method - choose one: bogo, bubble, bucket, heap, insertion, merge, radix, selection, smooth, quick')
            exit(0)
    else:
        print('(!) -- Error - invalid sorting method - choose one: bogo, bubble, bucket, heap, insertion, merge, radix, selection, smooth, quick')
        exit(0)

    anim = animation.FuncAnimation(
        fig,
        animateFunc,
        repeat=False,
        blit=False,
        frames=frames,
        interval=1000
    )
    plt.show()


if __name__ == '__main__':
    main()
