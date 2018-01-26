# Python3
# Author: George Hartoularos
# UCSF BMI203 Algoirthms Winter 2018
# Homework 1

import numpy as np
import random

def isinputcool(seq,lo=None,hi=None):
    '''
    Function checks quality of input for both main functions before
    performing algorithms
    '''
    trivial = False

    # catch a non-list
    try:
        seq = list(seq)
    except:
        print('Input: not iterable.')
        trivial = True
        return trivial, None

    # catch non-finite data
    try:
        if False in np.isfinite(seq):
            print('Input: sequence has invalid object type(s).')
            trivial = True
            return trivial, None
    except:
        print('Input: sequence has invalid object type(s).')
        trivial = True
        return trivial, None

    # catch empty data
    if len(seq) == 0:
        print('Input: sequence is empty, nothing to sort.')
        trivial = True
        return trivial, None

    # catch a trivial case
    if list(set(seq)) == [seq[0]]: # detect trivial case of equal elements
        trivial = True
        return trivial, seq

    return trivial, None

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(seq):
    
    """
    Function goes element-by-element through the list, and 
    determines if the element after it is bigger or smaller. If 
    smaller, it defines a new list with the 2 elements in question 
    switched. Will repeat this until the list is no longer out of 
    order. Then one final edge run confirms the list is ordered. 
    Returned list is in increasing order, smallest elements first, 
    biggest elements last.
    """
    trivial, val = isinputcool(seq)
    if trivial == True and val != None:
        return val
    elif trivial == True:
        return

    unordered = 1 # initialize unordered
    while unordered == 1:
        unordered = 0 # initialize to ordered, give it a chance!
        for i in range(len(seq)):
            prefix = seq[:i] # beginning part of list
            comp0 = [seq[i]] # left element for comparison
            try: # this will error if at end of list
                comp1 = [seq[i+1]] # right element for comparison
                suffix = seq[(i+2):] # end part of list
            except: # you've reached the end of the list, leave the for loop
                break
            if comp0[0] > comp1[0]: # simple comparison
                unordered = 1 # the list is unordered, cycle through again
                # make new list in modified order:
                seq = np.concatenate((prefix,comp1,comp0,suffix))
    return seq

def quicksort(seq,lo=0,hi='whole'):
    """
    Function takes in a sequence, start and end point to sort the elements of 
    the sequence between and including start and end. Start and end are 
    required for algorithm, but will default to entire sequence if no start 
    and end indices are passed. Initiate 'pivot' at start (first element by 
    default or at the index passed to 'lo') and initiate cursors immediately 
    to right of pivot (i) and at furthest point from pivot (j). Inch the 
    cursors closer to each other until they (1) reach a value greater than (i)
    and less than (j) the pivot, or (2) they hit each other. If (1) switch the
    elements at i and j and continue, or if (2) switch the elements at pivot 
    and collision point and stop. This guarantees that the pivot is now in 
    its sorted position, regardless of the order of the elements below and 
    above it. Then simply recursively apply this to the former and latter
    portions of the sequence (left and right of the pivot) until the sequence
    is of length 1, which is by definition ordered.
    """
    trivial, val = isinputcool(seq)
    if trivial == True and val != None:
        return val
    elif trivial == True:
        return

    if hi == 'whole': # extract the index of the last element
        hi = len(seq) - 1

    '''
    Need to nest in a larger function so that I can use input data quality checks,
    else checks will be run on every recursive call to function.
    '''
    def quicksorter(seq,lo,hi): 
        '''
        Define the partition function that will place the pivot in the correct
        position and *partition* the function into two smaller sequences
        '''
        def partition(seq,lo,hi):
            pivot = seq[lo] # define pivot
            i = lo + 1 # left cursor
            j = hi # right cursor
            while True: # do until break when j < i (collision)
                while i <= j and seq[i] <= pivot:
                    i += 1 # inch up
                while seq[j] >= pivot and j >= i:
                    j -= 1 # inch down
                if j < i:
                    break
                else: # store temporary variable k to swtich elements efficiently
                    k = seq[i]
                    seq[i] = seq[j] # do the switch
                    seq[j] = k
            k = seq[lo] # same storing for k above to swtich
            seq[lo] = seq[j]
            seq[j] = k
            return j # j becomes the cusp of the new sequences
        if lo < hi: # stop recursion
            pivot = partition(seq,lo,hi)
            quicksorter(seq,lo,pivot-1) #recursive calls of subsequence
            quicksorter(seq,pivot+1,hi)
        return seq
    return quicksorter(seq,lo,hi) # gotta return something



