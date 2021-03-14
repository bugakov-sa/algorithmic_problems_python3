from typing import List

class Solution:
    def count_nums(self, nums):
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        return res

    def checkTriplet(self, num1, num2, num3, nums_counts):
        if not (num3 in nums_counts):
            return False
        triplet_nums_counts = self.count_nums([num1, num2, num3])
        for num in triplet_nums_counts:
            if nums_counts[num] < triplet_nums_counts[num]:
                return False
        return True

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_counts = self.count_nums(nums)
        sorted_unique_nums = sorted(nums_counts.keys())
        for i in range(0, len(sorted_unique_nums)):
            for j in range(i, len(sorted_unique_nums)):
                num1 = sorted_unique_nums[i]
                num2 = sorted_unique_nums[j]
                num3 = 0 - num1 - num2
                if num3 >= num2:
                    if self.checkTriplet(num1, num2, num3, nums_counts):
                        res.append((num1, num2, num3))
                else:
                    break
        return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))