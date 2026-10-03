str1="AbcDEfghIJ"  
print(str1.upper())  #The upper() method convert a string to uppercase.

str1="AbcDEfghIJ"    #The lower() method converts a string to lower case.
print(str1.lower())

str2=" Silver spoon "
print(str2.strip())  #The strip() method removes any white spaces before nd after the string

str3="Hello World!!!   "
print(str3.rstrip(" !"))
print(str3.rstrip(" !"))  # Hello World

str2="Silver Spoon"
print(str2.replace("Sp","M"))
print(str2)

str2="Tanish"
print(str2.replace("Tan","Pri"))

str2="Silver Spoon"
print(str2.split(" ")) #splits the string at the white spaces
print(str2)

str1="hello"
print(str1.capitalize())

str1="Silver Spoon"
lst_str1=str1.split()
print(lst_str1)
print(type(str1))
print(type(lst_str1))

str2="hello world"
cpstr2=str2.capitalize()
print(cpstr2)
print(type(str2))
print(type(cpstr2))

str1="Welcome to the comsole"
cen_str1=str1.center(50)
print(cen_str1)
print(len(cen_str1[27]))