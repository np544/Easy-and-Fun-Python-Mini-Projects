str=input("Enter full meaning of an organization or concept or something. I'll acronymize it for you!!\n")
str=str.title()
newstr=""
for i in str:
    if i.isupper():
        newstr+=i
print("The acronym is "+newstr)