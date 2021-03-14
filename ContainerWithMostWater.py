class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        s = (j - i) * min(height[i], height[j])
        while j > i:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            new_s = (j - i) * min(height[i], height[j])
            if new_s > s:
                s = new_s
        return s
