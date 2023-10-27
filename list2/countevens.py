#%%

def count_evens(nums):
    c=0
    for i in nums:
        if i%2==0:
            c+=1
    return c


count_evens([2, 1, 2, 3, 4]) 