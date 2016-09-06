#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    #Iterate of the list for the length of the list -1. It is -1
    #because the range starts at 0.
    for i in range(len(lst)-1):
        swap=False
        #-i here so that you do not check what has already been sorted
        #keeping in mind with bubble sort the largest numbers bubble
        #to the end as it recurses, so subtracting i allows you to 
        #not check those that have already bubbled to the end. 
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                #Swapping because the left is bigger than the right. 
                lst[j], lst[j+1] = lst[j+1],lst[j]
                swap=True
        if not swap:
            #If swap is False when you get here, then the list is 
            #sorted. This will happen when it goes back to the top
            #of the outter loop. If the 'if' condition is not satisfied
            #in that loop, swap will remain False and it will break. 
            break




def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    pass


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    pass




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print