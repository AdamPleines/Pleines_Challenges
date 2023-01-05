def addTwoNumbers(l1, l2):
# I had to resist the urge to spend time 'reversing the numbers' before adding, which would have made things much harder...
# Apparently I did the whole thing in a method that is applicable to lists, but not 'linked lists'. Guess I'm gonna comment out my functional list code and see if I can do linked list stuff now... :/
    l3 = []
# find the min length to avoid 'out of range' errors
    if len(l1) >= len(l2):
        min_len = len(l2)
    else:
        min_len = len(l1)
# perform the additions for the equivalent ranges
    for i in (range(min_len)):
        l3.append(l1[i]+l2[i])
# add the remainder of the larger list, if applicable
    if len(l1) > len(l2):
        for j in range(len(l2),len(l1)):
            l3.append(l1[j])
    elif len(l2) > len(l1):
        for j in range(len(l1),len(l2)):
            l3.append(l2[j])
# adjust any values above 9 back to single digit, carry the 1 ;) 
    for k in range(len(l3)):
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
    l1 = []
    l2 = [0,5]
    answer = addTwoNumbers(l1, l2)
    print(answer)

if __name__ == '__main__':
    main()