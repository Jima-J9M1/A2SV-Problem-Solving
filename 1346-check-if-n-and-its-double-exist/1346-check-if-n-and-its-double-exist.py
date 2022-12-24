class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for index in range(len(arr)):
            val = 2 * arr[index]
            if  val != 0 and val in arr:
                return True
            elif val == 0 and (arr.count(val) > 1):
                return True
        return False
        