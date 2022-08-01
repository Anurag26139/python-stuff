class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        oldMap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in oldMap:
                return [oldMap[diff],i]
            oldMap[n]=i
        return
            