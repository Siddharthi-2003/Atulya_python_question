class solution (object):
    def find_duplicate(self,nums):
         a = nums[0]
         b = nums[0]
         while True :
             a = nums[nums[a]]
             b =nums[b]
             if a==b:
                 break
         ptr = nums[0]
         while ptr!=b:
                    ptr=nums[ptr]
                    b= nums[b]
         return ptr
ob1 = solution()
print(ob1.find_duplicate([3,2,3,4,6,])) 