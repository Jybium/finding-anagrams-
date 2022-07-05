def Anogram_check(str1, str2):  
    # Strings are sorted and check whether both are matching or not  
    if(sorted(str1)== sorted(str2)):  
        print("Both strings are an Anagram.")  
    else:  
        print("Both strings are not an Anagram.")  

## driver code 
str1 = str(input("enter the first word:"+" "))
str2 = str(input("enter the second word:" + " "))
print("the first word you entered is:" + " " ,str1)
print("the second word you entered is:" + " " ,str2)
Anogram_check(str1, str2)      