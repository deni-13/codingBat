def near_hundred(n):
    return True if (n>=90 and n <=110) or (n>110  and n<=210 ) else False


#solution
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))