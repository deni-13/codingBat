# https://codingbat.com/prob/p108886

#%%
"""
nums=[1, 2, 2, 6, 99, 99, 7]

t=0
for i in nums:
    if i==6:
        break
    t+=i

print(t)
 #yanlis 
"""
#%%

def sum67(nums):
    t=0
    add=True
    for i in nums:
        if i==6:
            add=False  #cik
        elif add:
            t+=i
        elif i==7 and not add:  #false
            add=True  #devam et
    return t
sum67([1, 2, 2, 6, 99, 99, 7])