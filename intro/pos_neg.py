
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True
#pos_neg(1, 1, True) → False
#pos_neg(1, 1, False) → False

#%%

def pos_neg(a, b, negative):
    return True if (a <0 and b <0)== negative else False
pos_neg(1, -1, False)
#pos_neg(-4, -5, True)

#-1 - 1 ngeatif false: ---> false  ikisi neggatif ise neg == true 
#-1 -1 : negatif  : true -- > true
# 1 -1 : negatif true -->  false
# 1 -1 : negatif false -->  false

# 1 1  : "  " --> false
# 1  1 : neg false: --> true  #ikiside neg degil neg =false 


#%%

def pos_neg(a, b, negative): 
  if negative: # 1  negative booleana gore cevirdik
    return (a < 0 and b < 0)  #ikisi negatif olan boolean 
  else:   #ikiside farkliysa 
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
  
print(pos_neg(1, 1, False))

