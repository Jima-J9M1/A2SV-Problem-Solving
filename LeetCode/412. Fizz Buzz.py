class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        s=[]
        for i in  range(1,n+1):
            if i%3==0:
                if i%15==0:
                    s.append("FizzBuzz")
                else:
                    s.append("Fizz")
            elif i%5==0:
                if i%15==0:
                    s.append("FizzBuzz")
                else:
                    s.append("Buzz")
            else:
                s.append(str(i))
        
        return s
            
        
