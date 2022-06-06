class solution:
    def solve(self, nums):
        max =0
        length= len(nums)
        for i in range(0,length-1):
            count=1
            for j in  range(i+1,length):
                if(nums[i]==nums[j]):
                    count+=1
                    if(max<count):
                        max=count
        return max
ob =solution()
nums=[1,5,8,5,3,5]
print(ob.solve(nums))                        