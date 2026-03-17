class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        h = len(img)
        w = len(img[0])
        
        ans = [[0]*w for _ in range(h)]
        
        for i in range(h):
            for j in range(w):
                s = 0
                cnt = 0
                
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni = i + di
                        nj = j + dj
                        
                        if 0 <= ni < h and 0 <= nj < w:
                            s += img[ni][nj]
                            cnt += 1
                
                ans[i][j] = s // cnt
        
        return ans