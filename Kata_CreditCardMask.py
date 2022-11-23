def persistence(cc):
    cc = str(cc)
    # strings are not mutable, so I made a new string that gets built (as desired) as the code goes along
    if len(cc) > 4:
        newstring = ''
        for i in range(len(cc)):
            if i+4 < len(cc):
                newstring = newstring + '#'
            else:
                newstring = newstring + cc[i]
    else:
        newstring = cc
    cc = newstring
    return cc

def main():
    cc = "try to codify this, or suffer defeat!"
    answer = persistence(cc)
    print(answer)

if __name__ == '__main__':
    main()