class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        power_of_two = []

        modulo = 10**9 + 7
        value = 1
        
        #store all power of two from 1 - 2**21         
        while value <= (2**21):
            power_of_two.append(value)
            value *= 2
            

            
        
        food_items = defaultdict(int)
        count_good_meal = 0
        
                 
        for ele in deliciousness:
            
            # count if the element found in the collection of previous element                                            differnce with power of two                 
            if ele in food_items:
                count_good_meal += food_items[ele]
            
            # store the difference between the element from all power of two
            for new_ele in power_of_two:
                val = new_ele - ele
                food_items[val] +=1 
         
        
        return count_good_meal % modulo

        
'''     
        power_of_two = []
        food_value = defaultdict(int)

        modulo = 10**9 + 7     
        ans = 0
        for val in deliciousness:

            for j in range(22):
                k = 2**j-val
                

                if k in food_value:
                    ans += food_value[k]

            food_value[val] += 1

'''
                    
        
                               



        
        