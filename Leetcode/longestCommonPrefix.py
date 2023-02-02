def longestCommonPrefix(strs):
    rets = ''
    shortest = 0 # starts at 0 in the case of an empty str in the list
    for a in range(len(strs)):
        if strs[a] == False:
            return rets
        elif len(strs[a]) < len(strs[shortest]):
            shortest = a
    for c in range(len(strs[shortest])): # c=string loop
        for b in range(len(strs)): # b=list loop
            if strs[b][c] == strs[shortest][c]:
                continue
            else: return rets
        rets = rets + strs[b][c]
    return rets

if __name__ == '__main__':
    strs = ['flower', 'flow', 'flags']
    ans = longestCommonPrefix(strs)
    print(ans)