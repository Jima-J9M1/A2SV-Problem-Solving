class Solution:
    def find(self, rep, size, x):
        root = x
        
        while root != rep[root]:
            root = rep[root]
            
        while x != root:
            parent = rep[x]
            rep[x] = root
            x = parent
            
        return root
    
    def union(self, rep, size, x, y):
        rep_x = self.find(rep, size, x)
        rep_y = self.find(rep, size, y)
        
        if rep_x == rep_y:
            return 
        
        if size[rep_x] > size[rep_y]:
            rep[rep_y] = rep_x
        
        elif size[rep_y] < size[rep_x]:
            rep[rep_x] = rep_y
            
        else:
            rep[rep_x] = rep_y
            size[rep_y] += 1
            
      
        
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #goal: merge account that have same email and return account in sorted emial, any account order
        #Two account has the same not mean have the same account.
        #Two account has the same email means the same name and also has one the same account
        '''
         e.g
            ["John","johnsmith@mail.com","john_newyork@mail.com"] 
            ["John","johnsmith@mail.com","john00@mail.com"]
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
            
            4 accounts if two account have the same phone and check if the have the same email 
            if the account have both same and can be merged
            account 1 and account 2 have the same name and same email account
            ["John", "johnsmith@mail.com","john_newyork@mail.com","john00@mail.com" ]
        '''
        
        #Algorithm to find the same account and merge them 
        #find account that have the same name and account and connect both account with the same representative to do that we need to helper function find and union to connect and find the representative
        # find accounts that have the same representative and merge those accounts and sort each account email
        # return the accounts
        #Time Complexity (1000) * (1000)
        n = len(accounts)
        representative = {i : i for i in range(n)}
        owner = {}
        size = [1] * n

        
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in owner:
                    self.union(representative, size, i, owner[email])
                    
                owner[email] = i
                
        ans = defaultdict(list)
        for email, rep in owner.items():
            rep = self.find(representative, size, rep)
            ans[rep].append(email)
            
            
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
        
        
                    
                    
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        