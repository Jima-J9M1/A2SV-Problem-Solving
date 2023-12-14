class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        names = defaultdict(list)
        ans = []
        
        
        for tran in transactions:
            name, minute, amount, city = tran.split(',') # alice 20 2000 mtv
            names[name].append([int(minute), city])
            
        for tran in transactions:
            name, minute, amount, city = tran.split(',')
            
            if int(amount) > 1000:
                ans.append(tran)
                continue
                
            for name_val in names[name]:
                minute_2, city_2 = name_val
                if abs((int(minute) - minute_2)) <= 60 and city != city_2:
                    ans.append(tran)
                    break
                    
                    
        
        return ans
                
                
            
            
        