thisdict={"brand":"Ford","model":"Mustang","year":1964}
print(thisdict)

print(len(thisdict))

print(thisdict["model"])
print(thisdict["year"])

for i in thisdict:
    print(i,thisdict[i],sep='-')

print(thisdict.get("brand"))

x=thisdict.keys()
print(x)

y=thisdict.values()
print(y)

for k,v in thisdict.items():
    print(k,v)
    
thisdict["colour"]="RED"
print(thisdict)
print("color" in thisdict)
print("model" in thisdict)