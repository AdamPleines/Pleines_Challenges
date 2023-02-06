# I noticed immediately that the n was unnecessary for python... so I ignored it.I got much better stats on submitting the commented code, despite directly more steps & memory use?
# def shuffle(nums):
#     l1 = []
#     l2 = []
#     ans = []
#     half = int(len(nums)/2)
#     for a in range(half):
#             l1.append(nums[a])
#             l2.append(nums[a+half])
#             ans.append(l1[a])
#             ans.append(l2[a])
#     return ans

def shuffle(nums,n):
    ans = []
    for a in range(n):
            ans.append(nums[a])
            ans.append(nums[a+n])
    return ans

if __name__ == '__main__':
    nums = [2,5,1,3,4,7]
    n=3
    ans = shuffle(nums, n)
    print(ans)