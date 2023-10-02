
# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2
#%%
#evet buda calisiyor
a="xxcodecodexxcode"
sp=[]
for i in a.split("co"):
    #print(i)
    sp.append(i)
print(sp)
say=0
for j in range(len(sp)):
    if len(sp[j])>1 and sp[j][1]=="e":
        say+=1
        print(sp[j])
print(say)

#onceki yazilan startswith blogunu cikardim ne olursa olsun
#burda baslasın veya baslamasin co ile gelenleri ayirdim ve
#bos eleman gelmesi yani "" --> bunu len ile kontrol ettim eger 



#     if sp[j][1]=="e" and len(sp[j])>1:
#         say+=1
# print(say)

#%%
def count_code(str):
    sp=[]
    for i in str.split("co"):
        print(i)
        sp.append(i)
    print(sp)
    sp.remove("") #calisiyor olamazsin :p
    say=0
    for j in range(0,len(sp)):
        if sp[j][1]=="e":
            say+=1
    return say

a="xxxcodexxcode"  #xxx patladi :D  
count_code(a)

# %%
