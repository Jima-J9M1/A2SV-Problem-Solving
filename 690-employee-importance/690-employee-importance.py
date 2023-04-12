"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_val = [0]
        
        for ele in employees:
            if ele.id == id:
                self.dfs(ele,employees, 0, total_val)
                
        return total_val[0]
        
    def dfs(self,emp, employee, curr_sum, total_val):
        total_val[0] += emp.importance
            
        for sub in emp.subordinates:
            for ele in employee:
                if ele.id == sub:
                    self.dfs(ele,employee, curr_sum, total_val)
                
        # total_val[0] = curr_sum