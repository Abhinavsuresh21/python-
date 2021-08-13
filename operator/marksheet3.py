name=input("Enter name:")
mark1=int(input("Enter english mark:"))
mark2=int(input("Enter tamil mark:"))
mark3=int(input("Enter maths mark:"))
mark4=int(input("Enter physics mark:"))
mark5=int(input("Enter chemistry mark:"))
mark6=int(input("Enter computer mark:"))
total=mark1+mark2+mark3+mark4+mark5+mark6;
avg=total/6;
print("\t\t marksheet \n\n")
print("english mark is",mark1)
print("tamil mark is",mark2)
print("maths mark is",mark3)
print("physics mark is",mark4)
print("chemistry mark is",mark5)
print("computer mark is",mark6)
print("total is",total)
print ("average is",avg)
if((mark1>=35)and(mark2>=35)and(mark3>=35)and(mark4>=35)and(mark5>=35)and(mark6>=35)):
    print("The person is pass")
else:
    print("the person is fail") 