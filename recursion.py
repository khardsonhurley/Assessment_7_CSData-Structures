# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """
    ######### NON RECURSIVE #########
    # for n in my_list:
    #     print n 

    ######### RECURSIVE APPROACH #1  ######### 
    #base case : if the length of the list is 1. 
    # if len(my_list) == 1:
    #     print my_list[0]
    #     return

    # #progress
    # first_number = my_list[0]

    # print first_number

    # rest_of_list = my_list[1:]
    
    # print_item(rest_of_list)

    ######### RECURSIVE APPROACH #2  #########
    first_number = my_list[0]

    print first_number

    rest_of_list = my_list[1:]
    
    #This is the base case [if the sliced list is empty, return, otherwise recurse.]
    if rest_of_list:
        print_item(rest_of_list)
    else:
        return


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """
    ######### NON RECURSIVE #########
    # print tree.data

    # for child in tree.children:
    #     print child.data

    ######### RECURSIVE #########

    #Base case: If there is nothing in the tree, it will return. 
    if not tree.data:
        return
    
    #Otherwise, print the data. 
    print tree.data

    #Thinking here that if the tree has no children, to return. But dont
    #think its necessary, because if the list is empty it will not go
    #into the for loop anyway. Thoughts?     
    if not tree.children:
        return 

    for child in tree.children:
        print_all_tree_data(child)


    

# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    ######### NON RECURSIVE #########
    # count = 0

    # for n in my_list:
    #     count = count + 1
    
    # return count

    ######### RECURSIVE #########
    count = 0

    #Base Case: The list is empty
    if not my_list:
        return 0

    #Progress: Slice the list adding one each time. 
    return 1 + list_length(my_list[1:])

    #THINKING: 
    # my_list = [1, 2, 3, 4]
    # list_length(my_list)
        # return 1 + list_length([2, 3, 4])
    # list_length(my_list)  
        # return 1 + list_length([3, 4])
    # list_length(my_list)
        # return 1 + list_length([4])
    # list_length(my_list)
        # return 1 + list_length([])
    # list_length(my_list)
        # return 0
    # 1 + 0 = 1
    # 1 + 1 = 2
    # 2 + 1 = 3
    # 3 + 1 = 4

# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
    """

    count = 0

    #Base Case: NOTE: Not sure if this works, but this idea here is that the tree has no
    #data in it. 
    if not tree.data:
        return count

    #Progress: If the node is not without data, up the count, to count that node.    
    count = count + 1

    #If the node does not have children, it will return count. 
    for child in tree.children:
        count = count + 1
        num_nodes(child)

    return count


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
