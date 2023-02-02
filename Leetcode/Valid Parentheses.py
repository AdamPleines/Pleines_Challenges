def isValid(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()','').replace('[]','').replace('{}','')
    print(s)
    print(len(s))
    print(type(s))
    return True if len(s)==0 else False # couldn't assess by type because it was written in/for python2 and all unicode, causing strange functionality.

# my original attempt. It was not clear if [{}] situations should be valid until first submission

    # val1 = ['[','{','(']
    # val2 = [']','}',')']
    # skip=0
    # # seems leetcode answers completely forgot to assess
    # for a in range(len(s)):
    #     if skip==1:
    #         skip=0
    #         continue
    #     elif a <= len(s)-2:
    #         if s[a] in val1 and s[a+1] in val2:
    #             if s[a]==val1[0]
    #                 if s[a+1] in val1 and s[a]!=s[a+1] and a+1 <= len(s)-3:
    #                     if s[a+1] in val1 and s[a]!=s[a+1]:
                            
    #                     elif s[a+1]==val2[0]:
    #                     skip=1
    #                     continue 
    #                 elif s[a+1]==val2[0]:
    #                     skip=1
    #                     continue

    #             elif s[a]==val1[1] and s[a+1]==val2[1]:
    #                 skip=1
    #                 continue
    #             elif s[a]==val1[2] and s[a+1]==val2[2]:
    #                 skip=1
    #                 continue
    #             else: return False
    #     else: return False
    # return True

if __name__ == '__main__':
    s = '[{}]()'
    ans = isValid(s)
    print(ans)