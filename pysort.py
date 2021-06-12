import sys
import matplotlib.pyplot as plt
from time import sleep
from matplotlib import animation
from random import random

def barlist(): 
    return random()

fig = plt.figure()

frames = 1000
x = range(1,101)
barcollection = plt.bar(x, 1)

def animate(i):
    y = barlist()
    for a, b in enumerate(barcollection):
        b.set_height(y)

anim = animation.FuncAnimation(
    fig,
    animate,
    repeat=False,
    blit=False,
    frames=frames,
    interval=100
)

plt.show()












# Bogo Sort
# def bogoSort(num1, num2):

# Bubble Sort


# Bucket Sort


# Heap Sort


# Insertion Sort


# Merge Sort


# Radix Sort


# Selection Sort


# Smooth Sort


# Quick Sort


# def main():
#     args = sys.argv
#     if (len(args) > 1):
#         if (args[1] == 'bogo'):
#         elif (args[1] == 'bubble'):
#         elif (args[1] == 'bucket'):
#         elif (args[1] == 'heap'):
#         elif (args[1] == 'insertion'):
#         elif (args[1] == 'merge'):
#         elif (args[1] == 'radix'):
#         elif (args[1] == 'selection'):
#         elif (args[1] == 'blur'):
#         elif (args[1] == 'smooth'):
#         elif (args[1] == 'quick'):
#         else:
#             print('(!) -- Error - invalid sorting method - choose one: bogo, bubble, bucket, heap, insertion, merge, radix, selection, smooth, quick')
#             exit(0)
#     else:
#         print('(!) -- Error - invalid sorting method - choose one: bogo, bubble, bucket, heap, insertion, merge, radix, selection, smooth, quick')
#         exit(0)

# if __name__ == '__main__':
#     main()
