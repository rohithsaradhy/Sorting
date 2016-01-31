# written by Rohith Saradhy on 18-1-2016
# Computation Physics Lab Work on learning Quick Sort


import random

def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] > A[j]: # Swapping if A[i] > A[j]
                dum = A[j]
                A[j] = A[i]
                A[i] = dum
    return A






def main():
    # Getting the length of the List
    N = int(raw_input("Please Enter the list size N \n"))
    print " You Entered", N
    # Defining Random List of size N
    RList = []
    for i in range(0, N):
        RList.append(int(random.random() * 10000))
    # Printing the List
    for i in RList:
        print i
    # Running Quick Sort
    sorted_list = bubble_sort(RList)
    # Printing it out
    print("********")
    print "After Sorting"

    for i in sorted_list:
        print i


if __name__ == "__main__":
    main()