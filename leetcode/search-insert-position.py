class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1
        i = 0
        
        while a <= b:
            i = (a + b)//2
            if nums[i] < target:
                a = i + 1
            elif nums[i] > target:
                b = i - 1
            else:
                return i
        return i + 1 if target > nums[i] else i
        