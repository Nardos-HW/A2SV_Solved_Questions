class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.sum_ = [0]
        t = 0
        for i in nums:
            t += i
            self.sum_.append(t)
    
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        
        return (self.sum_[right+1]-self.sum_[left])

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)