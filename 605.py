def canPlaceFlowers(places, n):
    if n == 0:
        return True
    for i in range(len(places)):
        if places[i] == 0 and (i == 0 or places[i-1] == 0) and (i == len(places)-1 or places[i+1] == 0):
            places[i] = 1
            n -= 1
            if n == 0:
                return True
    return False
    
    
print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))