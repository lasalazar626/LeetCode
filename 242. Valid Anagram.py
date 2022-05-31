
def isAnagram(s,t):
        hash = {}
        for char in s:
            if char not in hash:
                hash[char] = 1
            else:
                hash[char] +=1
        for char in t:
            if char not in hash:
                return False
            else:
                if hash[char] ==1:
                    hash.pop(char)
                else:
                    hash[char]-=1
        return True if len(hash)==0 else False





