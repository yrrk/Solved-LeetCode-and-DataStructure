#tring Rotation: Assume you have a method isSubString which checks if one word is a substring of another.
#Given two strings, S1 snd S2, write code to check if S2 is rotation of S1 using only one call to isSubString
#eg: "waterbottle" is a rotation of "erbottlewat"


def isSubString(S1,S2):
    bigstring=S1+S1
    
    if S2 in bigstring:
        return True
    else:
        return False
    
    
String1="waterbottle"
String2="erbottlewat"

print(isSubString(String1,String2))