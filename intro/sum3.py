def sum3(nums):
    if len(nums)==3:
        topl=0
        for i in nums:
            topl+=i
    return topl

#%%
def sum3(nums):
    return sum(nums)


#%%%
def rotate_left3(nums):
  return [nums[1] ,nums[2] ,nums[0]]

rotate_left3([1, 2, 3]) 