def fun(Abirth,Bbirth):
    Aby = Abirth[0:4]
    Abm = Abirth[4:6]
    Abd = Abirth[6:8]
    Bby = Bbirth[0:4]
    Bbm = Bbirth[4:6]
    Bbd = Bbirth[6:8]
    if Aby>Bby:
        print("B大")
    elif Aby < Bby:
        print("A大")
    else:
        if Abm > Bbm:
            print("B大")
        elif Abm < Bbm:
            print("A大")
        else:
            if Abd > Bbd:
                print("B大")
            elif Abd < Bbd:y
                print("A大")
            else:
                print("A和B同样大")
print("请输入A的生日(格式例如20180101)")
Abirth = input()
print("请输入B的生日(格式例如20180101):")
Bbirth = input()
fun(Abirth,Bbirth)
#-----------------------------分割-----------------------------
import random
A = []
for i in range(10):
    a = random.choice(range(10))
    A.append(a)
print(A)
b = random.choice(range(10))
if b in A:
    print(b)
    print("有")
else:
    print(b)
    print("没有")