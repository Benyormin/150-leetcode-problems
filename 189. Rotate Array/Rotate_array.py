class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if( len(nums) == 1):
            return
        if( k > len(nums)):
            k = k % len(nums)
        temp = []
        i = len(nums) - k 
        while (i < len(nums)):
            temp.append(nums[i])
            i += 1
        #shift array to the right 
        i = len(nums) - k - 1 
        while(i >= 0):
            nums[i+k] = nums[i]
            i -= 1
        #rotate others ( out of bounds)
        i = 0
        while(i<k):
            nums[i] = temp[i]
            i += 1
        