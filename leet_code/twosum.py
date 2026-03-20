nums = [11,7,2,15]
target = 9



def twoSum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in lookup:
            return [lookup[diff], i]

        lookup[num] = i
        


print(twoSum(nums,target))