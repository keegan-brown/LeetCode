class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lookAhead = 1
        n = len(nums)
        i = 0
return

        for i in range(n):
            if nums[i] == nums[i+lookAhead]:                
                nums[i] = nums[i+1]
                lookAhead+=1
            if i + lookAhead > n:
                break