
# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'
#%%
c1=""
c="kitten"

c1+="".join(c).replace(c[1],"")

print(c1)


#%%
def missing_char(str, n):

    c1=""

    c1+="".join(str).replace(str[n],"")

    return(c1)


str="kitten"
missing_char(str,4)
