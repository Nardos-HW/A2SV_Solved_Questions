class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        
        i = rStart
        j = cStart
        
        steps = 1
        
        while len(res) < rows * cols:
            
            for _ in range(steps):
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
                j += 1
            
            for _ in range(steps):
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
                i += 1
            
            steps += 1
            
            for _ in range(steps):
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
                j -= 1
            
            for _ in range(steps):
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
                i -= 1
            
            steps += 1
        
        return res[:rows * cols]
        