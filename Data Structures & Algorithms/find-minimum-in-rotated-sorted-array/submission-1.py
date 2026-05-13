class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minNum = float('inf')
        while l <= r:
            mid = (l+r)//2
            if nums[l] < nums[r]:
                return min(nums[l],minNum)
            else:
                minNum = min(nums[mid],minNum)
                if nums[mid] >= nums[l]:
                    l = mid +1 
                else:
                    r = mid -1
        return minNum
