class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        passed = set()
        nums.sort()
        res = []
        
        i = 0
        
        while i < len(nums) - 2:
            if nums[i] in passed:
                i+=1
                continue
            
            p1,p2 = i+1,len(nums)-1
            curr_num = nums[i]
            
            while p1<p2:
                sum = curr_num+nums[p1]+nums[p2]

                if sum<0:
                    p1+=1

                elif sum>0:
                    p2-=1

                else:
                    res.append([curr_num, nums[p1], nums[p2]])
                    p1+=1
                    
                    while p1<p2 and nums[p1] == nums[p1-1]:
                        p1+=1
                
        
            passed.add(nums[i])
            i+=1

        return res
            
