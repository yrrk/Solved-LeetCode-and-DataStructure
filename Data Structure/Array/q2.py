#Given two strings, write a method to decide if one is permutation of the other



def permutableString(string1,string2):




    #Using sort method
    SortedString1=sorted(string1)
    SortedString2=sorted(string2)
    
    if(SortedString1==SortedString2):
        return True
    else:
        return False









    #Using count method
    # count=0
    # if(len(string1)==len(string2)):
    #     for char in string1:
    #         if(char in string2):
    #             count+=1
    # if(count==len(string2)):
    #     return True
    # else:
    #     return False
    
    
    
    
    
    
    
    
    
    
print(permutableString('abcd','dbca'))