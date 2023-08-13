class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        #goal: return minimun raduis 
        #[1,2,3] [2] 1 -> 2(2) -> 3
        #edge case: one house and many heaters 
        #edge case: one heater and one house
        
        
        # algorthim to find the minimum raduis
        # sort both houses and heaters list
        # pick one house and find the minimum raduis to warm the house
        # store each house's minimu radius form the heaters
        # find a house that has max radius from the list of each house's radius
        # return the max radius 
        
        min_radius = float("-inf")
        heaters.sort()
        houses.sort()
        
        for house in houses:
            left = 0
            right = len(heaters) - 1
            
            while left < right:
                mid = left + (right - left)// 2
                
                if house >= heaters[mid]:
                    left = mid + 1
                else:
                    right = mid
                    
            if left - 1 < 0:
                radius  = abs(house - heaters[left])
                min_radius = max(min_radius, radius)
            else:
                radius1 = abs(house - heaters[left]) 
                radius2 = abs(house - heaters[left - 1])
                min_radius = max(min_radius, min(radius1, radius2))
                
        return min_radius
            
         