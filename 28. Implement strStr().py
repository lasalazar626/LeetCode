def strStr(self, haystack: str, needle: str) -> int:
        end = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i:i+end] == needle:
                return i
        return -1