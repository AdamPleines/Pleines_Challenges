# Tried out using exception handling while practicing. Turns out its fairly versatile and easy to pickup. The round function, however, defies basic math logic for 'friendlier/balanced' approximates.
# This is either failing the complexity limit or is getting caught in the leetcode system. It works here nearly instantly, so I'm guessing its the latter.
def searchInsert(nums, target):
    length = len(nums)
    if len(nums) == 0:
        return 0
    if len(nums)==1:
        if nums[0] >= target:
            return 0
        else: return 1
    found = False
    point = int(.5*(length)+.5)
    # print('mind the edge')
    try:
        while found == False:
            # print(point)
            if target == nums[point]:
                # print('target is ', target,' while numpt = ',nums[point])
                return point
            elif point == 0:
                if nums[0]>target:
                    return 0
                elif nums[0]<target:
                    return 1
            elif nums[point] < target and nums[point+1] > target:
                return point+1
            elif nums[point] > target and nums[point-1] < target:
                # print('returned?')
                return point
            elif target > nums[point]:
                # print(point)
                point = int(point/2+.5) + point
                # print('greater target')
                # print(point)
            elif target < nums[point]:
                point = point - int(point/2+.5)
                # print('lesser target')
    except IndexError:
        # print('out of index:')
        if point==0:
            if nums[0]>target:
                return 0
            elif nums[0]<target:
                return 1
        elif point==len(nums)-1:
            return point+1
    return point

if __name__ == '__main__':
    target = 0
    nums = [1,3,5,6]
    ans = searchInsert(nums, target)
    print('ans =', ans)