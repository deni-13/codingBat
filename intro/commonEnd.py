
# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True
#%% denemelerrrr! boyuta bakmaksizin burda once ortaklari aldim sonra
#ilk ve son elemanlari ortak olanlarla  karsilastirdim
lis1=[1, 2, 3]
lis2=[7,3,2]
lis=[]
for i in lis1:
    for j in lis2:
        if i==j:
            lis.append(i)

print(lis)
print(lis[-1])

if (lis[-1] ==lis1[-1]) and ( lis[-1]  ==lis2[-1]) or lis[0]==lis1[0] and lis[0]==lis2[0]:
    print( "True")

else:
    print(" False")

#%% funct
def common_end(a,b):
    lis=[]
    for i in a:
        for j in b:
            if i ==j:
                lis.append(i)

    if (lis[-1] ==a[-1]) and ( lis[-1]==b[-1]) or ((lis[0]==a[0]) and (lis[0]==b[0])):
        return True
    else:
        return False
