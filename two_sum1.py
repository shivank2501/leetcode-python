def twoSum(l,target):
    m = {}
    for i,n in enumerate(l):
        diff = target - n
        if diff in m:
            return [m[diff],i]
        m[n] = i    


l = [1,2,3,4]
target = 6

print(twoSum(l,target))