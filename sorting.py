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
    return lst




def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    new_list = []

    #Checking for empty lists here. 
    while len(list1)>0 or len(list2)>0:
        #If list 1 is empty, then add the first element of list 2. Popping it off. 
        if not list1:
            new_list.append(list2.pop(0))
        #If list 2 is empty, then add the first element of list 1. Popping it off.
        elif not list2:
            new_list.append(list1.pop(0))
        #If the first element in list 1 is bigger than the first element in list 2, 
        #then pop the first element of list two and append it to the result list. 
        elif list1[0]>list2[0]:
            new_list.append(list2.pop(0))
        #Otherwise pop the first element of list one and append it to the result list. 
        else:
            new_list.append(list1.pop(0))

    return new_list





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
    #Base Case: What is the list only has one item in it? 
    if len(lst) < 2: 
        return lst

    #Take the length of the list and divide it by two. If it returns a float (like 3.5)
    #then return the integer value of that (rounding down which would be 3). This is the 
    #index at which the partition will occur. 
    middle = int(len(lst)/2)

    #Partition the list around the middle index. 
    list1 = lst[:middle]
    list2 = lst[middle:]

    #Apply merge sort again (find the middle and partition.) This will continue to happen
    #Until the partitioned list has only one item in it. At that point it will call the function
    #merge_lists, which compares the element of each single item list and pops the smallest into the front
    #of new_list. This happens until the entire list is sorted. 
    list1= merge_sort(list1)
    list2= merge_sort(list2)

    new_list = merge_lists(list1, list2)

    return new_list









#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print