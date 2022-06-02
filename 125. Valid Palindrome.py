def isPalindrome(self, s: str) -> bool:
        chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        temp = ""
        for char in s.lower():
            if char in chars:
                temp+=char
        for i in range((len(temp))//2):
            if temp[i] != temp[len(temp)-1-i]:
                return False
        return True