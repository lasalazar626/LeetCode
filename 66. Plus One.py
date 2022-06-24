class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i >= 0:
            digits[i] +=1
            if i == 0 and digits[i] == 10:
                digits[i] = 1
                digits.append(0)
                return digits
            elif digits[i] == 10:
                digits[i] = 0
                i-=1
            else:
                return digits
