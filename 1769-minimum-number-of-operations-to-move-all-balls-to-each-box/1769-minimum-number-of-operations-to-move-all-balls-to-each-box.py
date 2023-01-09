class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        length = len(boxes)
        
        #count number of steps to store the ball in each boxes
        for index in range(length):
            sum_of_steps = 0
            for j in range(length):
                
                if index == j:
                    continue
                if boxes[j] == "1":
                    sum_of_steps += abs(index - j)
            ans.append(sum_of_steps)
            
        return ans