class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        min_rad = float('inf')
        def checker(mid):
            i = 0
            j = 0
            while i < len(houses) and j < len(heaters):
                if houses[i] >= heaters[j] - mid and houses[i] <= heaters[j] + mid :
                    i += 1
                else:
                    j += 1
                if j >= len(heaters) and i < len(houses):  
                    return False 
            return True

        low = 0
        high = max(houses[-1] - heaters[0], heaters[-1] - houses[0])
        while low <= high:
            mid = (low + high) //2
            print(mid, low , high)
            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low



