class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_soldier = defaultdict(list)
        
        for indx,row in enumerate(mat):
            count = row.count(1)
            num_soldier[count].append(indx)
            
        result = []
        for key in sorted(num_soldier.keys()):
            result.extend(sorted(num_soldier[key]))
            
            
        return result[:k]