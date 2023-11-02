class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        #Give: Transaction -> name, time, amount, city 
        #Give: Conditions that can invalid the transaction -> x: x > 1000 and 
        #      the transcation -> (minute, name, city) | (< 60, name, city)  
        indices = set()
        nameOfTrans = defaultdict(list)
        
        for tran in transactions:
            name, minute, amount, city = tran.split(",")
            nameOfTrans[name].append([int(minute), city])
            
        
        ans = []
        for tran in transactions:
            name, minute, amount, city = tran.split(",")
            
            if int(amount) > 1000:
                ans.append(tran)
                continue
                
            if name in nameOfTrans:
                for t, c in nameOfTrans[name]:
                    if abs(int(minute) - t) <= 60 and city != c:
                        ans.append(tran)
                        break
                        
               
        return ans
                
#         for indx,tran in enumerate(transactions):
#             name, minute, amount, city = tran.split(",")
              
#             if int(amount) > 1000:
#                 indices.add(indx)
                
#             for j in range(indx + 1, len(transactions)):
#                 name2, minute2, amount2, city2 = transactions[j].split(",")
                
#                 if int(amount2) > 1000:
#                     indices.add(j)
                    
#                 if name2 == name and city != city2 and abs(int(minute2) - int(minute)) <= 60:
#                     indices.add(indx)
#                     indices.add(j)
                    
                    
#         indices = sorted(list(indices))
        
#         res = []
        
#         for indx in indices:
#             res.append(transactions[indx])
            
            
#         return res
            