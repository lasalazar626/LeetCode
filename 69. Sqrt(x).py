def mySqrt(x) -> int:
        if x == 1 or x == 0:
            return x
        L,R = 0 ,x
        while L <= R:
            mid = L + (R-L)//2
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            elif mid*mid > x:
                R = mid
            elif mid*mid < x:
                L = mid
            
            
        return temp