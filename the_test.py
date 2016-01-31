# written by Rohith Saradhy on 18-1-2016
# Computation Physics Lab Work on learning Quick Sort
import timeit
import random
from bubble_sort import bubble_sort
from quick_sort import quick_sort


# Testing the code for different List size
N = range(0,1000,5)
# time to record the complexity for quick sort and bubble sort
time_quick = []
time_bubble = []

for n in N:
    # Creating a random list of n numbers
    RList = []
    for i in range(0, n):
        RList.append(int(random.random() * n))
    # timing it for quick sort and bubble sort and adding it time_quick and time_bubble respectively
    t = timeit.Timer(lambda: quick_sort(RList))
    time_quick.append(t.timeit(number=1))
    t = timeit.Timer(lambda: bubble_sort(RList))
    time_bubble.append(t.timeit(number=1))

#writing a final file with Columns being Operations, Time-Quicksort, Time-Bubblesort

f = open('dataset.txt','w')
for i in range(0,len(N)):
    f.write(str(N[i])+"  " + str(time_quick[i]) + "  " + str(time_bubble[i]) + "  " + "\n")
f.close()

