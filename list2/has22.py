#%% https://codingbat.com/prob/p119308

def has22(k):
    s=""
    for i in k:
        s+="".join(str(i))
    #print(s)
    if "22" in s:
        return True 
    return False


has22([1, 2, 2])

# has22([1, 2, 1, 2])
#has22([2, 1, 2])  