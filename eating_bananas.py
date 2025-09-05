import math
def minEatingSpeed(piles, h) -> int:
        left, right = 1, max(piles)
        result = 0
        while left <= right :
            middle = (left + right) // 2
            hours_spent = 0
            for p in piles :
                hours_spent += math.ceil(p / middle)
            if hours_spent <= h :
                result = middle
                right = middle - 1
            else :
                left = middle + 1     
        return result
piles = [3,6,8,11]
h = 8
print(f" The min eating rate of bananas : {minEatingSpeed(piles, h)}")