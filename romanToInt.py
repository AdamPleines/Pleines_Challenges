# I realized later how there was a simple relationship between the out-of-sequence large numbers (IV -> V-I = 4). That could have drastically shortened the code. At least this shows I was writing this myself...

def romanToInt(s):
    value = 0
    skip = 0
    validl = ['I','V','X','L','C','D','M']
    if type(s) == str and len(s) >= 1 : # going to check for the proper symbols later. Delete the type == str part if doing in OOP code and do a try -> exception assessment. This code isn't OOP, so no issues here.
        for l in range(len(s)):
            print(value)
            print(l)
            if skip == 1:
                skip = 0
                continue
            elif l <= len(s)-2 and s[l] in validl: # s[l] == 'I' or s[l] == 'V' or s[l] == 'X' or s[l] == 'L' or s[l] == 'C' or s[l] == 'D' or s[l] == 'M':
                if s[l] == 'M':
                    value = value + 1000
                elif s[l] == 'D':
                    value = value + 500
                elif s[l] == 'C' and s[l+1] == 'M':
                    value = value + 900
                    skip = 1
                elif s[l] == 'C' and s[l+1] == 'D':
                    value = value + 400
                    skip = 1
                elif s[l] == 'X' and s[l+1] == 'C':
                    value = value + 90
                    skip = 1
                elif s[l] == 'X' and s[l+1] == 'L':
                    value = value + 40
                    skip = 1
                elif s[l] == 'I' and s[l+1] == 'X':
                    value = value + 9
                    skip = 1
                elif s[l] == 'I' and s[l+1] == 'V':
                    value = value + 4
                    skip = 1
                elif s[l] == 'C' and s[l+1] != 'M' and s[l+1] != 'D':
                    value = value + 100
                elif s[l] == 'L':
                    value = value + 50
                elif s[l] == 'X' and s[l+1] != 'C' and s[l+1] != 'L':
                    value = value + 10
                elif s[l] == 'V':
                    value = value + 5
                elif s[l] == 'I' and s[l+1] != 'X' and s[l+1] != 'V':
                    value = value + 1
            elif l == len(s)-1:
                if s[l] == 'M':
                    value = value + 1000
                if s[l] == 'D':
                    value = value + 500
                if s[l] == 'C':
                    value = value + 100
                if s[l] == 'L':
                    value = value + 50
                if s[l] == 'X':
                    value = value + 10
                if s[l] == 'V':
                    value = value + 5
                if s[l] == 'I':
                    value = value + 1
            else: return 'Error?'
        return value
    elif type(s) != str:
        return 'Invalid input!'    
    else: return value

def main():
    s = 'LVIII'
    value = romanToInt(s)
    print(value)

if __name__ == '__main__':
    main()