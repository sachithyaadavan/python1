id=1000
name="Seelan"
age=30
print("my id is",id+)
print("my name is",name)
print("my age is",age)

name=input()
id=input()
age=input()
print("my name is",name,"\nmy id is",id,"\nmy age is",age)
print(type(id))

id=1000
name="Seelan"
age=30
print("my id is",id)
print("my name is",name)
print("my age is",age)
print(type(id))
output=f"my id is{id}\nmy name is{name}\nmy age is{age}"
print(output)
output="my id is{}\nmy name is{}\nmy age is{}".format(id,name,age)
print(output)
output="my id is{0}\nmy name is{1}\nmy age is{2}".format(id,name,age)
print(output)
print("my id is %d\nmy name is %s\nmy age is %d"%(id,name,age))
