class Solution(object):
    
    def __init__(self):
        self.cumulative_hash = {0:1}
    
    def subarraySum(self, nums, k):
        sum = 0
        count= 0

        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum - k in self.cumulative_hash :
                  count = count + self.cumulative_hash[sum-k]
            if sum in self.cumulative_hash:
             self.cumulative_hash[sum] += 1
            else:
             self.cumulative_hash[sum] = 1
            


        return count

print(Solution().subarraySum([0,0,0],0))
    
      
            
 