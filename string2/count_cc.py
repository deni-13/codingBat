def count_code(s):
    count = 0
    for i in range(len(s) - 3):
        if s[i:i+2] == "co" and s[i+3] == "e":
            count+=1
        return count

a = "copexxxxcodexxcode"
result = count_code(a)
print(result)


#%% eksik solution CARPİİİİİİİİİİİİİİİİİ
def count_code(str):
    sp=[]
    if not str.startswith("co"):
        for i in str.split("co"):
            #print(i)
            sp.append(i)
        print(sp)
        say=0
        for j in range(0,len(sp)):
            if (len(sp[j])>1) and (sp[j][1]=="e"):
                say+=1
        return say
    else:
        return str.count("co")

a="ccccxxxcopexxxxcodexxcode"
count_code(a)
#%% ve CALİSTİ OOOK

def count_code(str):
    sp=[]

    for i in str.split("co"):
        #print(i)
        sp.append(i)
    print(sp)
    say=0
    for j in range(0,len(sp)):
        if (len(sp[j])>1) and (sp[j][1]=="e"):
            say+=1
    return say

# a="ccccxxxcopexxxxcodexxcode"
a="codecocdcodecodecopecore"
count_code(a)