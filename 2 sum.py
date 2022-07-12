nums=[2,7,11,15]
target=9
n=nums[0]
oldMap={}
for i,n in enumerate(nums):
    diff=target-n
    if diff in oldMap:
        print(oldMap[[diff], i])
    oldMap[n]=i
print(oldMap) 
