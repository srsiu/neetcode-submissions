class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        left_max = [0] * len(height)
        right_max = [0] * len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)-1):
            left_max[i] = max(left_max[i-1], height[i])
        right_max[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        max_trapped = 0
        for i in range(len(height)-1):
            max_trapped = max_trapped + (min(left_max[i], right_max[i]) - height[i])
        return max_trapped
            

        