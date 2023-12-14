class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        invalid = []
        
        transactions_time = defaultdict(dict)
        
        for tran in transactions:
            name, time, amount, city = tran.split(',')
            time = int(time)
            if name not in transactions_time[time]:
                transactions_time[time][name] = {city, }
            else:
                transactions_time[time][name].add(city)
                
        
        print(transactions_time)
        for tran in transactions:
            name, time, amount, city = tran.split(',')
            time = int(time)
            if int(amount) > 1000:
                invalid.append(tran)
                continue
                
                
            for range_time in range(time - 60, time + 61):
                if range_time not in transactions_time:
                    continue
                    
                if name not in transactions_time[range_time]:
                    continue
                    
                transaction_by_time = transactions_time[range_time][name]
                
                if city not in transaction_by_time or len(transaction_by_time) > 1:
                    invalid.append(tran)
                    break
                    
                    
                
            
            
        return invalid
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         invalid = []

#         # Record all transactions done at a particular time
#         #   including the person and the location.
#         transaction_time = defaultdict(dict)
#         for transaction in transactions:
#             name, str_time, amount, city = transaction.split(",")
#             time = int(str_time)

#             if name not in transaction_time[time]:
#                 transaction_time[time][name] = {city, }
#             else:
#                 transaction_time[time][name].add(city)

#         for transaction in transactions:
#             name, str_time, amount, city = transaction.split(",")
#             time = int(str_time)

#             # # check amount
#             if int(amount) > 1000:
#                 invalid.append(transaction)
#                 continue

#             # # check if person did transaction within 60 minutes in a different city
#             for inv_time in range(time-60, time+61):
#                 if inv_time not in transaction_time:
#                     continue
#                 if name not in transaction_time[inv_time]:
#                     continue

#                 trans_by_name_at_time = transaction_time[inv_time][name]

#                 # check if transactions were done in a different city
#                 if city not in trans_by_name_at_time or len(trans_by_name_at_time) > 1:
#                     invalid.append(transaction)
#                     break

#         return invalid

                
                
            
            
        