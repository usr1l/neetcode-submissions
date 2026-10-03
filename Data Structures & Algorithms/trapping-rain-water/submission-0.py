class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        total_vol = 0

        while left<right:
            curr_min=min(max_left, max_right)
            if height[left] <= height[right]:
                left+=1
                max_left = max(height[left], max_left)
                if curr_min - height[left] > 0:
                    total_vol += curr_min-height[left]

            else:
                right-=1
                max_right = max(height[right], max_right)
                if curr_min - height[right] > 0:
                    total_vol += curr_min-height[right]

   
        return total_vol


        

        
