
#if esle statment
marks=70
if marks==100:
    print("good")
elif marks<100:
    print("normal")
else:
    print("bad")
food=input("enter your food:")
eat="yes" if food=="cake" else "no"
print("eat")
h="apple"
print("sweet") if h=="apple" or h=="banana" else "not sweet"
age=56
 #vote=("yes","no")[age<18] not valid only in vs cocde
 #string
n="barshha"
print(len(n))
t=" i am barsha"
print(t.endswith('ha'))
print(t.capitalize())
print(t.replace("a" ,"i"))
print(t.find("barsha"))
#dictionary
you= {
    "name" :"barsha",
    "subject" : ["c","c++"],
    "age" :19,
    "num":7749817939
}
print(you)
print(list(you.keys()))
#loop
i=1
while i<5:
   print("heyy")
   i=i+1
j=1
while j<=10:
        print(3*j)
        j=j+1
        n=[4,8,2,1,6,7]
        idx=0
        while idx<=len(n)-1:
            print(n[idx])
            idx+=1
            #for loop
            l=[75,98,34,32]
            for num in l:
                print(num)
            else:
                print("end")
                for e in range(1,5,2):
                    pass
                if e==3:
                     print(e)
                     #function in python
                     def calculate (x,y):
                        print(x*y)
                     calculate(6,4)
                     #recursion
                     def show(n):
                        if(n==0):#base case
                             return
                        print(n)
                        show(n-1)
                        print("end")

        show(3)
                    # this is a new line##this is second line# this is a new line