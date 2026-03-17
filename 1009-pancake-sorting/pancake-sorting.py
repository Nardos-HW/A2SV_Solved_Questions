class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            idx = arr.index(size)
            
            if idx != size - 1:
                if idx != 0:
                    arr[:idx+1] = arr[:idx+1][::-1]
                    res.append(idx+1)
                
                arr[:size] = arr[:size][::-1]
                res.append(size)
        
        return res