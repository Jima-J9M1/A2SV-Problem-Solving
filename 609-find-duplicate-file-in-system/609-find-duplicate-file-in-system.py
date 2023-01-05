class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        file = defaultdict(list)
        length = len(paths)
        ans = []
        #find the file name and store all directory and file type in the file dictionary          
        for ele in paths:
            file_path = list(map(str,ele.split()))
            directory = file_path[0]
            
            for index in range(1,len(file_path)):
                pointer = file_path[index].index('(')
                file[file_path[index][pointer+1:-1]].append(directory+"/"+file_path[index][:pointer])
        
        
        for ele in file.values():
            if len(ele) > 1:
                ans.append(ele)
        
        return ans
            
            