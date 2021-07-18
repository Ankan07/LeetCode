class Solution(object):
    
    def __init__(self):
        self.sum = 0
    
    def subarraySum(self, nums, k):
       startIndex =0
       endIndex = startIndex
       self.sum = nums[0]
       i=0
       count = 0
    
       while startIndex <=len(nums)-1 and endIndex<=len(nums)-1:
            if self.sum < k:
              endIndex+=1
              if endIndex <= len(nums)-1:
                self.calculateSum(endIndex,'end',nums)
            else:
                if self.sum == k:
                  count = count+1
                self.calculateSum(startIndex,'start',nums)
                startIndex+=1
       return count
            
    def calculateSum(self,index,type,nums):
        if type == 'start':
         self.sum -= nums[index]
        if type == 'end':
         self.sum += nums[index]


print(Solution().subarraySum([1,2,3],2))