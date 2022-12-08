#One Away: There are three types of edits that can be performed on string: insert a character, remove a character, or replace a character.
#Given two strings, write a function to check if they are one edit or zero edit away

def OneAway(string1,string2):
    if(string1==string2):
        return True
    elif(len(string1)==len(string2)):
        return checkreplacement(string1,string2)
    elif(len(string1)==len(string2)+1):
        return checkinserted(string2,string1)
    elif(len(string2)==len(string1)+1):
        return checkinserted(string1,string2)
    else:
        return False

#To check the replacement
def checkreplacement(s1,s2):
    count=0
    hashstring1={}
    for i in range(len(s1)):
            hashstring1[i]=s1[i]
    for item in s2:
        if(item not in hashstring1.values()):
            count+=1
    if(count>1):
        return False
    else:
        return True




#To check the inserted text
def checkinserted(s1,s2):
    edited=False
    i=0
    j=0
    
    while(i<len(s1) and j<len(s2)):
        if(s1[i]!=s2[j]):
            if(edited):
                return False
            edited=True
            j+=1
        else:
            i+=1
            j+=1
    return True
    
print(OneAway("yaksh","yalwh"))



