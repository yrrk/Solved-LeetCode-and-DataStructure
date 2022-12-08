# Implement an algorithm to determine if a string has all unique characters


def uniqueitem(word):
    hashedWord={}
    count=0
    for char in word:
        count+=1
        if(char not in hashedWord.values()):
            hashedWord[count]=char
    
    if(count==len(hashedWord)):
        return True
    else:
        return False










    #By Using sort method
    # sortedWord=sorted(word)
    # for i in range(len(sortedWord)-1):
    #     if(sortedWord[i]==sortedWord[i+1]):
    #         return False       
    # return True
    







    # Brute Force
    # for i in range(len(word)):
    #     for j in word[i+1:]:
    #         if(word[i]==j):
    #             return "unique item found"
                
    # return "no unique item found"
            
            
        

print(uniqueitem('yaksh'))