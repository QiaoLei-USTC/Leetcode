import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num=np.array(nums)
        size=num.size
        x=np.tile(num,(size,1))
        y=x.transpose()
        sum=x+y
        indall=np.argwhere(sum==target)
        ind1=indall[:,0]
        ind2=indall[:,1]
        ind=indall[ind1<ind2,:]
        return ind.tolist()
