#String Compression: implement a metho to perform basic string compression using the counts of repeated characters.
#For example, the string aabcccccaaa would become a2b1c5a3


def StringCompress(string1):





    #Solution according to the textbook
    count=0
    compressedstring=''
    for i in range(len(string1)):
        if(i!=0 and string1[i]!=string1[i-1]):
            compressedstring=compressedstring+string1[i-1]+str(count)
            count=0
        count+=1
    compressedstring=compressedstring+string1[-1]+str(count)
    if(len(compressedstring)<len(string1)):
        return compressedstring
    else:
        return string1









    #Self done
    # count=0
    # temp=''
    # compressedstring=''
    # for i in string1:
    #     if(temp==''):
    #         temp=i
    #         count+=1
    #     else:
    #         if(temp==i):
    #             count+=1
    #         else:
    #             compressedstring=compressedstring+temp+str(count)
    #             temp=i
    #             count=1
    # compressedstring=compressedstring+temp+str(count)
    # return compressedstring
    
    

print(StringCompress('aabcccccaaaeeeeee'))