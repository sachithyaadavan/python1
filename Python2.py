Studentid=3001
Studentname="Seelan"
Grade=12 
NICnumber=200503758829
print("Student id is",Studentid)
print("Studnet name is",Studentname)
print("Grade is",Grade)
print("NIC number is",NICnumber)
print(type(id))
output=f"Studentid is {Studentid}\nStudentname is {Studentname}\nGrade is {Grade}\nNICnumber is {NICnumber}"
print(output)
output="Studentid is{}\nStudentname is {}\nGrade is {}\nNICnumber is {}".format(Studentid,Studentname,Grade,NICnumber)
print(output)
output="Studentid is{0}\nStudentname is {1}\nGrade is {2}\nNICnumber is {3}".format(Studentid,Studentname,Grade,NICnumber)
print(output)
output=("Studentid is " +str(Studentid)+"\nStudentname is "+ Studentname+"\nGrade is "+str(Grade)+"\nNICnumber is "+str(NICnumber))
print(output)
print("Studentid is %d\nStudentname is %s\nGrade is %d\nNICnumber is %d"%(Studentid,Studentname,Grade,NICnumber))

