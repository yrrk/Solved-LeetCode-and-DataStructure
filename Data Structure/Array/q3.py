#URLify: Write a method to replace all spaces in a string with "%20". 
#You may assume that the string has sufficient spacew at the end to hold the additional character
#You are given the true length of the string


def Urlify(string1):




    #Without using list
    finalstring=string1.rstrip()
    output=""
    for i in range(len(finalstring)):
        if(finalstring[i]==' '):
            output=output+"%20"
        else:
            output=output+finalstring[i]
    return output














    # Using lists to URLify the string and remove the trailing spaces
    # finalstring=string1.rstrip()
    # liststring=list(finalstring)
    
    # for i in range(len(liststring)):
    #     if(liststring[i]==' '):
    #         liststring[i]="%20"
        
    # string1=''.join(liststring)
    
    # return string1
    
print(Urlify('my name is yaksh         '))