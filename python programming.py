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