numbers = [1,2,3,4,5]
target = 7

def twoSum2(numbers,target):
    l,r = 0,len(numbers) -1
    while l<r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l,r]
        elif s < target:
            l +=1
        else:
            r -=1

print(twoSum2(numbers,target))                     