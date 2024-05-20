from classes import *
P1 = Person("", "", "")
e=0
P1.name=input("Digite o nome da pessoa: ")
while e!=7:
    e = int(input(f"O que {P1.name} irá fazer? \n1.COMER | 2.FALAR | 3.DORMIR | 4.PARAR DE COMER | 5.PARAR DE FALAR | 6.PARAR DE DORMIR | 7.SAIR\n"))
    while e<1 or e>7:
        print("Valor inválido. Digite as opções de acordo com o MENU:")
        e = int(input(f"O que {P1.name} irá fazer? \n1.COMER | 2.FALAR | 3.DORMIR | 4.PARAR DE COMER | 5.PARAR DE FALAR | 6.PARAR DE DORMIR | 7.SAIR\n"))
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
