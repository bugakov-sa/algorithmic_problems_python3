from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def count_nums(nums):
            res = {}
            for i in range(0, len(nums)):
                if nums[i] in res:
                    res[nums[i]] += 1
                else:
                    res[nums[i]] = 1
            return res

        nums_counts = count_nums(nums)

        def checkQuadruplet(num1, num2, num3, num4):
            if not (num4 in nums_counts):
                return False
            nums_counts_quadruplet = count_nums([num1, num2, num3, num4])
            for num in nums_counts_quadruplet.keys():
                if nums_counts_quadruplet[num] > nums_counts[num]:
                    return False
            return True

        sorted_unique_nums = sorted(nums_counts.keys())
        res = set()
        for i in range(0, len(sorted_unique_nums)):
            for j in range(i, len(sorted_unique_nums)):
                for k in range(j, len(sorted_unique_nums)):
                    num1 = sorted_unique_nums[i]
                    num2 = sorted_unique_nums[j]
                    num3 = sorted_unique_nums[k]
                    num4 = target - num1 - num2 - num3
                    if num4 >= num3:
                        if checkQuadruplet(num1, num2, num3, num4):
                            res.add((num1, num2, num3, num4))
                    else:
                        break
        return res

print(Solution().fourSum([1,0,-1,0,-2,2], 0))