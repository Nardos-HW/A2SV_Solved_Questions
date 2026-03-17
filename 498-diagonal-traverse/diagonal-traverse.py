class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r = len(mat)
        c = len(mat[0])
        
        out = []
        d = 1
        
        for s in range(r + c - 1):
            tmp = []
            
            for i in range(r):
                j = s - i
                if 0 <= j < c:
                    tmp.append(mat[i][j])
            
            if d:
                tmp.reverse()
            
            out.extend(tmp)
            d = 1 - d
        
        return out