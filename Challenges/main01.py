from classes import *
P1 = Person("", "", "")
e=0
P1.name=input("Enter the person's name: ")
while e!=7:
    e = int(input(f"What {P1.name} is going to try to do? \n1.Eat | 2.Talk | 3.Sleep | 4.Stop eat | 5.Stay silent | 6.wake up | 7.Leave Program\n"))
    while e<1 or e>7:
        print("Erro! try the options of the MENU:")
        e = int(input(f"What {P1.name} is going to try to do? \n1.Eat | 2.Talk | 3.Sleep | 4.Stop eat | 5.Stay silent | 6.wake up | 7.Leave Program\n"))
    if e == 1:
        P1.eat()
    elif e==2:
        P1.talk()
    elif e==3:
        P1.sleep()
    elif e==4:
        P1.stopEat()
    elif e==5:
        P1.stopTalk()
    else:
        P1.stopSleep()
