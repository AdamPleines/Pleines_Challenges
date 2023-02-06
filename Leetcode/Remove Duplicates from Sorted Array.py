def removeDuplicates(nums):
    a = sorted(set(nums))
    for b in range(len(a)):
        nums[b] = int(a[b])
        if len(a) >= 1:
            for c in range(len(nums)):
                if c > len(a)-1:
                    nums[c]='_'
    return nums

# I couldn't get this one to work properly in Python, due to an unexpected return type, then noticed the downvotes were greater than the upvotes and no solutions done in python...