#Palindrome Permutation: Given a string, with a function to check if it is a permutation of a palindrome.
#A palindrome is a word that is same forwards and backwards. A permutation is re-arrangement of letters.
#Palindrome not necessary should be limited to dictionary words


def PalinPermu(string1):
    hashmap={}
    
    
    for char in string1:
        if(char not in hashmap.keys()):
            hashmap[char]=1
        else:
            hashmap[char]+=1
        
    
    
    if(len(string1)%2==0 and len(string1)/2==len(hashmap)):
        return True
    elif(len(string1)%2!=0 and (len(string1)+1)/2==len(hashmap)):
        return True
    else:
        return False
        
    
print(PalinPermu('lolo'))