def singleNumber(nums) -> int:
        temp = 0
        for val in nums:
            temp^=val
        return temp
            