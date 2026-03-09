import random;

# All the variables:
vi=0
vf=0
a=0
x=0
t=0


print("Basic Physics Calculator")
while(True):
    print("1. Calculate kinematics equation")
    print("Please enter your desired option")
    option = int(input("Enter your option here: "))
    if(option == 1):
        print("\n\n")
        print("1: v0+at=vf\n 2: x=v0t+0.5at^2 \n 3: vf^2-vi^2=2ax")
        number = int(input("\n Please input the desired equation:"))
        if(number==1):
            condition = 0
            vi=int(input("put your vi: "))   
            vf=int(input("put your vf: "))
            t=int(input("put your t: "))
            print(" The acceleration is: " +str((vf-vi)/t))
            print("\n\n\n")
        elif(number ==2):
            condition = 0
            vi=int(input("put your vi: "))   
            t=int(input("put your t: "))
            a=int(input("put your a: "))
            print(" The displacement is: " +str((vi*t)+0.5*t*a^2))
            print("\n\n\n")
