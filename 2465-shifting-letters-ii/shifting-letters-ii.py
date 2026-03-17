class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        diff = [0] * (n + 1)
        
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val
        
        res = []
        curr = 0
        
        for i in range(n):
            curr += diff[i]
            shift = curr % 26
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            res.append(new_char)
        
        return ''.join(res)