class Solution:
    def maxArea(self, height: List[int]) -> int:
        L,R = 0,len(height)-1
        max = 0
        while L<R:
            if height[L]<height[R]:
                area = height[L]*(R-L)
                L+=1
                if area > max:
                    max = area
            else:
                area = height[R]*(R-L)
                R-=1
                if area > max:
                    max = area
        return max
