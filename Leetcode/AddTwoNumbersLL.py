# This is primarily to become accustomed to linked lists. Apparently the 'linked' difference is more pronounced in the code than I believed at first.
def construct_linked_list(list):
    class Node:
        def __init__(self, list):
            self.data = list
            self.head = Node
            self.next = next

def linked_list_counter(linked_list):
    count = 0
    list_head = linked_list.head
    while(list_head):
        count += 1
        # list head (reference location header) is the same as long as still within the same list.
        # advance to the next spot
        list_head = list_head.next
    return count

def addTwoNumbers(l1, l2):
    l1_length = linked_list_counter(l1)
    l2_length = linked_list_counter(l2)
    
    # need the min length to avoid 'out of range' errors
    if l1 >= l2:
        min_length = l2_length
        max_length = l1_length
        l3 = l2
    else:
        min_length = l1_length
        max_length = l2_length
        l3 = l1

    # now to actually add them together

    if l1_length == max_length:
        for j in range(min_length,max_length):
            l3.append(l1[j])
    elif l2_length == max_length:
        for j in range(min_length,max_length):
            l3.append(l2[j])
# adjust any values above 9 back to single digit, carry the 1 ;) 
    for k in range(max_length):
        if l3[k] > 9 and k < len(l3)-1:
            l3[k] = l3[k] - 10
            l3[k+1] = l3[k+1] + 1
        elif l3[k] > 9 and k == len(l3)-1:
            l3[k] = l3[k] - 10
            l3.append(1)
        elif l3[k] > 9:
            print('Error?')
    return l3
    



def main():
    list_1 = [9,1]
    list_2 = [1,5,7]
    l1 = construct_linked_list(list_1)
    l2 = construct_linked_list(list_2)
    answer = addTwoNumbers(l1, l2)
    print(answer)

if __name__ == '__main__':
    main()