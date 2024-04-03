#Project Love Calculator
print("Welcome to OCHIENG Love Calculator")
name1=input("What is your name?\n")
name2=input("What is your partner's name/crush?\n")
name_lower1=name1.lower()
name_lower2=name2.lower()
t=name_lower1.count("t")
r=name_lower1.count("r")
u=name_lower1.count("u")
e=name_lower1.count("e")
t1=name_lower2.count("t")
r1=name_lower2.count("r")
u1=name_lower2.count("u")
e1=name_lower2.count("e")
l=name_lower1.count("l")
o=name_lower1.count("o")
v=name_lower1.count("v")
e=name_lower1.count("e")
l2=name_lower2.count("l")
o2=name_lower2.count("o")
v2=name_lower2.count("v")
e2=name_lower2.count("e")
true=t+r+u+e+t1+r1+u1+e1
love=l+o+v+e+l2+o2+v2+e2
t=str(true)
l=str(love)
tl=t+l
tlove=int(tl)
if tlove<10 or tlove>90:
   print(f"Your love score is {tlove}%, you go together like coke and mentos!")
elif tlove>=40 and tlove<=50:
   print(f"Your love score is {tlove}%, you are alright together!")
else:
   print(f"Your love score is {tlove}%")
