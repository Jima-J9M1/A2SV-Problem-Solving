class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def whoWins(score,left,right,turn):
            
            if left == right:
                if turn:
                    return [score[left],0]
                else:
                    return [0,score[left]]
                
                
                
            if turn:
                
                
                right_score = whoWins(score, left,right - 1,False)
                right_score[0] += score[right]
                
                left_score = whoWins(score, left + 1,right,False)
                left_score[0] += score[left]
                
                if right_score[0] >= left_score[0]:
                    return right_score
                else:
                    return left_score
            else:
                
                right_score = whoWins(score, left,right - 1,True)
                right_score[1] += nums[right]
                left_score = whoWins(score, left + 1,right,True)
                left_score[1] += nums[left]
                
                if right_score[1] >= left_score[1]:
                    return right_score
                else:
                    return left_score
                
        
        result = whoWins(nums,0,len(nums) - 1,True)
        print(result)
        return result[0] >= result[1]
                