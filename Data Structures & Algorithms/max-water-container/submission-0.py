class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calculate_area(bar_a: int, bar_b: int, index_a:int, index_b:int):
            height = min(bar_a, bar_b)
            width = index_b - index_a
            return height * width
        
        index_a = 0
        index_b = len(heights) - 1 
        max_area = 0
        while index_a < index_b:
            max_area = max(
                max_area, 
                calculate_area(
                    heights[index_a],
                    heights[index_b], 
                    index_a, 
                    index_b
                )
            )
            if heights[index_a] > heights[index_b]:
                index_b -= 1
            else:
                index_a += 1
        return max_area