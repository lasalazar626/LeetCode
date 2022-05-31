def removeDuplicates(nums) -> int:
        # go through each element and compare to the next
        # if next is the same, we pop 
        i=0
        while i<len(nums):
            if i+1< len(nums) and nums[i+1] ==nums[i]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)