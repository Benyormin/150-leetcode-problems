class Solution:
    def removeDuplicates(self, nums) -> int:
        prev = nums[0]
        counter = 1 
        deleted = 0
        i = 1 
        temp = len(nums)
        while( i < len(nums)):
            if( nums[i] == prev):
                if( counter >= 2 ):
                    del[nums[i]]
                    deleted +=1
                    continue

                counter += 1
                prev = nums[i]
            else:
                counter = 1
                prev = nums[i]
            i +=1
        return temp - deleted
    
nums = [1,1,1,2,2,2]
c1 = Solution()
c1.removeDuplicates(nums)
print(nums)