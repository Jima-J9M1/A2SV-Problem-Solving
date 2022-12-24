class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return 0
        
        nums.sort()
        
        # three side to form traingle perimeter, use three pointer to indicate the sides
        side_1 = 0
        side_2 = 1
        side_3 = 2
        length = len(nums)
        perimeter = 0
        
        while side_3 < length:
            sum_two_side = nums[side_1] + nums[side_2]
            
            if sum_two_side > nums[side_3]:
                new_perimeter = sum_two_side + nums[side_3]
                
                perimeter = max(perimeter, new_perimeter)
            side_1 += 1
            side_2 += 1
            side_3 += 1
        
        return perimeter
        