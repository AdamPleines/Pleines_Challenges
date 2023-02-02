def isPalindrome(x):
    # negative & non-int cases are non-applicable for challenge
    if type(x) is int and x >= 0:
        # begin assessing if palindrome, by converting to a string for quick solution
        if int(str(x)[::-1]) == x:
            return True
        else: return False
    else: 
        return False

def isintPalindrome(x):
# negative & non-int cases are non-applicable for challenge
    if type(x) is int and x >= 0:
        # assessing if palindrome, avoiding use of str conversion (add challenge)
        revx = 0
        countx = x
        while countx > 0:
            revx = 10*revx + countx % 10
            countx = (countx-countx%10)/10
        if x == revx:
            return True
        else: return False
    else: return False

def main():
    x = 1223221
    answer = isintPalindrome(x)
    print(answer)

if __name__ == '__main__':
    main()