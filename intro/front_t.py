
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
    if len(str)>3:
        return n*str[0:3]  #3 krkterden buyukse 
    else:
        return  n*str
        
#%%alt:
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result