class Solution:
    def containsDuplicateFast(self, nums: List[int]) -> bool:
        if len(nums) != len(set(list(nums))):
            return True
        return False

    def containsDuplicateForce(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False