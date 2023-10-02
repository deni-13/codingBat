
# Given a string, return a new string where the first and last chars have been exchanged.


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

#%%
x="aavJ"

# 0 3 
# 1 2 


str1=""

str1=x[0:3:2]
str1
#str1[::-1]
str2=x[1::2]
str2

print(str2+str1[::-1])


#%%







#%%

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]
