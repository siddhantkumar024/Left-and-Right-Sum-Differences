class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s=0
        for num in nums:
            s+=num
        n=len(nums)
        leftsum=0
        rightsum=s
        p=[]
        for num in nums:
            rightsum-=num
            p.append(abs(leftsum-rightsum))
            leftsum+=num
        return p


        
