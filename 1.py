class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)): 
            #print (i, nums[i], len(nums))
            if(i+2<=len(nums)):
              for j in range(i+1,len(nums)):
                if ((nums[i]+nums[j])==target):
                  return (i,j)
            else:
              break
        