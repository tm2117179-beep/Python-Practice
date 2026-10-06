d={ "model":"Ford","model": "Mustang","Year":"2020"}
for i,j in d.items():
    print(i,j)

print("model"in d)

d.update({"color":"Red","city":"unnao","comtact":"999999"})  #ek sath bahut sare keys pair add kar sakte ho
print(d)

d.update({"model":"suzuki"})
print(d)

d["name"]="tanish"
print(d)

d.pop("model")
print(d)

d.popitem()
print(d)

d.clear()
print(d)

del d["year"]
print(d)