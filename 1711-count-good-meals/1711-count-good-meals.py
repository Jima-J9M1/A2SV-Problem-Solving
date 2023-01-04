class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        power_of_two = []
        food_value = defaultdict(int)
        ans = 0
        modulo = 10**9 + 7

        for val in deliciousness:

            for j in range(22):
                k = 2**j-val
                

                if k in food_value:
                    ans += food_value[k]

            food_value[val] += 1

        return ans % modulo
    
    
#         value = 2
        
#         while value <= (2**20):
#             power_of_two.append(value)
#             value *= 2

            
        
#         food_items = defaultdict(int)
#         count_good_meal = 0
        
#         for ele in deliciousness:
            
#             if ele in food_items:
#                 count_good_meal += food_items[ele]
                
#             for new_ele in power_of_two:
#                 val = new_ele - ele
#                 food_items[val]+=1

                    
        
                        
#         return count_good_meal



        
        