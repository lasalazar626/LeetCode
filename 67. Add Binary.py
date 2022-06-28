class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1,p2 = len(a)-1,len(b)-1
        carry = 0
        fin = ""
        while (p1>= 0 or p2 >=0):
            num1 = int(a[p1]) if p1 >= 0 else 0
            num2 = int(b[p2]) if p2 >= 0 else 0
            #print(f"rn we are adding {num1} and {num2} and {carry}")
            summer = num1 + num2 + carry
            carry = summer//2
            char = str(summer%2)
            fin = char+ fin
            p1 -=1
            p2 -=1
        if carry:
            fin = "1" + fin
        return fin
        
