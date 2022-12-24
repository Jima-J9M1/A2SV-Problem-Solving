class Solution:
    def average(self, salary: List[int]) -> float:
        
        #sort the salary list to find the minimum salaray and maximum salary
        salary.sort()
        
        #add the salary without including the minimum and maximum salary
        length = len(salary)
        left = 1
        right = length -1
        add_salary = sum(salary[left:right])
        ans = add_salary / (length - 2)
        
        return ans
        
        