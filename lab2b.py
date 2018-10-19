# Luis Ochoa
# 80508534


class Node(object):
    password = ""
    count = -1
    next = None
    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


# creates linked list with passwords and and sorts them in ascending order using bubble sort
def solution_A():
    f = open('test.txt')
    line = f.readline()
    list = Node(None,-1,None)
    while line:  # reads line by line to not run out of memory; gets only the passwords
        list = insert_A((line.split(None, 1)[1]).rstrip(), list)
        line = f.readline()

    f.close()
    # print_list(list)

    list = bubble_sort(list)
    print_top_20(list)


# creates dictionary of passwords then dumps into a linked list to sort it using merge sort
def solution_B():

    f = open('test.txt')
    line = f.readline()
    dict = {}
    while line:
        # getting only the passwords from each line
        dict = insert_B((line.split(None, 1)[1]).rstrip(), dict)
        line = f.readline()

    f.close()
    # dumping dictionary into list
    list = dict_to_node(dict)
    list = merge_sort(list)
    print_top_20(list)
    # print_list(list)


# used to obtain the length of a list
def lenlist(list):

    count = 0
    while list is not None:
        count += 1
        list = list.next
    return count


# used to test contents of lists/nodes
def print_list(list):

    while list is not None :
        print (list.password, list.count)
        list = list.next


# used by solution a to insert items into the list
def insert_A(str, list):

    temp_node = list
    # if it finds password it adds to counter, otherwise creates new node
    while temp_node.password is not None:
        if temp_node.password == str:
            temp_node.count += 1
            return list
        temp_node = temp_node.next
    new_node = Node(str, 0, list)
    list = new_node
    return list


# checks if password is present in dictionary and adds to counter, if not creates new bucket
def insert_B(str, dict):

    if str in dict:  # You can assume this operation takes O(1)
        dict[str] = dict[str] + 1
    else:
        dict[str] = 0

    return dict


# dumps dictionary and returns a linked list
def dict_to_node(dict):

    temp_node = None
    for key, val in dict.items():
        node_helper = Node(key,val,temp_node)
        temp_node = node_helper
    return temp_node


def bubble_sort(list):

    for i in range(lenlist(list)-1):
        # resets tempnodes to iterate through linked list again
        temp_node1 = list
        temp_node2 = list.next

        for j in range(lenlist(list)-1):

            if temp_node1.count < temp_node2.count:
                # changing contents of nodes if they are in wrong order
                node_helper_count = temp_node1.count
                node_helper_password = temp_node1.password
                temp_node1.password = temp_node2.password
                temp_node1.count = temp_node2.count
                temp_node2.password = node_helper_password
                temp_node2.count = node_helper_count
            # progressing through linked list
            temp_node2 = temp_node2.next
            temp_node1 = temp_node1.next
    return list


def merge_sort(list):
    # basa case
    if list is None or list.next is None or list.next.next is None:
        return list
    mid = lenlist(list)//2
    right = None

    node_helper = list
    left = list

    for i in range(mid):
        node_helper = node_helper.next
    # cutting linked list in half
    right = node_helper.next
    node_helper.next = None
    # merging back
    left = merge_sort(left)
    right = merge_sort(right)
    list = merge(left, right)
    return list


def merge(left, right):

    result = None
    if left is None:
        return right
    if right is None:
        return left
    if left.count > right.count:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)
    return result


def print_top_20(list):

    for i in range(20):
        print(i+1, list.password, "->", list.count)
        list = list.next


def main():

    solution_A()
    solution_B()

main()