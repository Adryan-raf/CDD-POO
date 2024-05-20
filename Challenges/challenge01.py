class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.talking = False
        self.eating = False
        self.sleeping = False

    def eat(self):
        if self.talking == True:
            print(f"{self.name} can't eat, cause is talking.")
        elif self.sleeping == True:
            print(f"{self.name} can't eat, cause is sleeping.")
        elif self.eating==True:
            print(f"{self.name} already was eating.")
        else:
            self.eating = True
            print(f"{self.name} is eating now.")

    def talk(self):
        if self.eating == True:
            print(f"{self.name} can't talk, cause is eating.")
        elif self.sleeping == True:
            print(f"{self.name} is talking while sleep.")
        elif self.talking==True:
            print(f"{self.name} already was sleeping.")
        else:
            self.talking = True
            print(f"{self.name} is sleeping now.")

    def sleep(self):
        if self.talking == True:
            print(f"{self.name} can't sleep, cause is talking.")
        elif self.eating == True:
            print(f"{self.name} can't sleep, cause is eating.")
        elif self.sleeping == True:
            print(f"{self.name} already was sleeping.")
        else:
            self.sleeping = True
            print(f"{self.name} is sleeping now.")
    
    def stopEat(self):
        if self.eating==False:
            print(f"{self.name} already wasn't eating.")
        else:
            self.eating = False
            print(f"{self.name} stoped of eat now.")
    def stopTalk(self):
        if self.talking==False:
            print(f"{self.name} already wasn't talking.")
        else:
            self.talking = False
            print(f"{self.name} is silent now.")
    def stopSleep(self):
        if self.sleeping==False:
            print(f"{self.name} already was awake.")
        else:
            self.sleeping = False
            print(f"{self.name} wake up now.")
