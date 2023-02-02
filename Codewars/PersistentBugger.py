def persistence(n):
    t = 0
    while len(str(n)) > 1:
        #some info, such as number of iterations (t), is required to be adjusted or reset each while loop
        size = len(str(n))
        t += 1
        d = 1
        stringed = str(n)
        # needed a list (or splice/array or something to iterate though) for ease of coding
        listed = []
        # i is equivalent to each string character in order... in need the range iteration to cycle through it though
        for i in stringed:
            listed.append(int(i))
        # 2nd loop required to iterate through the list, instead of assigning values into the list
        for j in range(size):
            d = d * listed[j-1]
        n = d
        print(n)  
    return t

def main():
    n = 48
    answer = persistence(n)
    print(answer)

if __name__ == '__main__':
    main()