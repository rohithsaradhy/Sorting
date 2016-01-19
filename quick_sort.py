# written by Rohith Saradhy on 18-1-2016
# Computation Physics Lab Work on learning Quick Sort


import random


def quick_sort(A):
    # Function for Quick Sort
    left = [] # Defining left array
    right = [] # Defining right array
    if len(A) > 1: # If len(A) > 1 then we print the length and choose a pivot(we take the middle element)
        # print("Length = " + str(len(A)))
        pivot = int(len(A) / 2)
        for item in range(0, len(A)): # Now we move items > than the pivot to left array and < than to right array
            if A[item] < A[pivot]:
                left.append(A[item])
            elif A[item] > A[pivot]:
                right.append(A[item])
        a_piv = A[pivot]

        # Commenting out for faster processing
        '''
        # Some Printing to check whether the code works
        print("----")
        print("pivot =" + str(a_piv))
        print("left =" + str(left))
        print("right =" + str(right))'''
        # We then use function recursion to sort the left and right arrays until there is only one element
        left = quick_sort(left)
        right = quick_sort(right)
        '''
        print("------")
        print("pivot =" + str(a_piv))
        print("left =" + str(left))
        print("right =" + str(right))'''
        # we append the pivot element back to the left array and concatenate left and right to get back the original array
        left.append(a_piv)
        A = left + right
        return A
    else: # If the len(A) < 1 then we return it back 
        return A

def main():
    # Getting the length of the List
    N = int(raw_input("Please Enter the List Size N \n"))
    print " You Entered", N
    # Defining Random List of size N
    RList = []
    for i in range(0, N):
        RList.append(int(random.random() * 1000000))
        # Printing the List
        for i in RList:
            print i
    # Running Quick Sort
    A = quick_sort(RList)
    # Printing it out
    print("********")
    print "After Sorting"

    for i in A:
        print i

if __name__ == "__main__":
    main()

