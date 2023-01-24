class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        sort_arr = sorted(arr)
        res = []
        i = -1
        
        if sort_arr == arr:
            return []
        
        max_val = max(arr)
        index = arr.index(max_val)
        if len(arr) - 1 != index:
            arr[:index + 1] = arr[:index + 1][::-1]
            res.append(index + 1)
            arr[:] = arr[::-1]
            res.append(len(arr))
        
        
        while arr != sort_arr:
            max_val = max(arr[:i])
            index = arr.index(max_val)
            
            if arr[index + 1] - arr[index] == 1:
                i -= 1
                continue
            else:
                val = arr[:index + 1][::-1]
                arr[:index+1] = val
                arr[:i]= arr[:i][::-1]
                i -= 1
                print(arr[:i+1])
                if len(arr) + i == 1 or index == 0:
                    res.append(len(arr[:i+1]))
                    continue

                res.append(index + 1)
                res.append(len(arr[:i + 1]))
            

        return res
            
