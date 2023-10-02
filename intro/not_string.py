
# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'
#%%
#1st way: indexing
def not_string(str):
    if str[0:3]==("not"):
        return str
    else:
        return("not"+" "+str)
    
	
not_string('is not')

# not_string("not bad")


#%% deneme dshdshf
# x="bad" #---> not bad
# x="is not"   #--- > not is not
# #="not bad"  --> not bad
x=
for  i in range(len(x)):
    if x[i]==" ":
        x=x.replace(" ", "not")
print(x)
#%%
#kucuk bir bilgilendirme: startswith de kullanilabilir
#2-startswith

def not_string(x):
    if x.startswith("not"):
        return(x)

    else:
        y="not" +" "+x

        return(y)

x="is not"
not_string(x)