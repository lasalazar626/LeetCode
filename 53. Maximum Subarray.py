class Solution:
    def maxSubArray(self, nums) -> int:
        curCount = 0
        maxCount = nums[0]
        for num in nums:
            curCount+=num
            if curCount<num:
                curCount=num
            maxCount = max(maxCount,curCount)
        return maxCount