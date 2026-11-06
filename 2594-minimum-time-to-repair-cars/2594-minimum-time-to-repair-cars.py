class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def checker(mid):
            toatl = 0
            for rank in ranks:
                cur= int(sqrt(mid/rank))
                if toatl < cars:
                    toatl += cur
            return toatl >= cars

                    
    
        low = 1
        high = 10 ** 18
        while low <= high:
            mid= (low+high)//2
            if checker(mid):
                high = mid-1
            else:
                low = mid+1
        return low