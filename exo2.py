import time
from exo1 import Robot
import random

class Human():
    __sexe = ['F','M']
    __list_aliment = []
    __aliment = ''

    @property
    def sexe(self):
      return self.__sexe
    
    @sexe.setter
    def sexe(self, sexe):
      self.__sexe = sexe

    @property
    def list_aliment(self):
      return self.__aliment
    
    @list_aliment.setter
    def list_aliment(self, list_aliment):
      self.__list_aliment = list_aliment

    @property
    def aliment(self):
      return self.__aliment
    
    @aliment.setter
    def aliment(self, aliment):
      self.__aliment = aliment

    """Human class content here"""
    def __init__(self, sexe):
        self.__sexe = sexe
        

    def add_aliment(self):
        temp = input('entrez aliment au menu :')
        self.__list_aliment.append(temp)


    def eat(self):
        for aliment in self.__list_aliment:
          print("eating", aliment)


    def digest(self):
        self.__list_aliment = []
        print("digested")

class Cyborg(Robot, Human):   
    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def cyberpsychosis(self):
        a = random.randrange(1,10)
        if a == 5 or a == 6:
            print("AHAHAHHAHAHH")
            for i in range(0,20):
                time.sleep(0.1) 
                print("s̴̠̒͋̈́̔p̶͚̘̪̥̗̳͕̍̑̒̌̌̿̂̔̿̚͜͝é̶̥̻͉̜̱̝͓̰̻̠́͌͑̇̿̂̾̓͊͜e̵̡̮̼̜̞̺͓͌͝d̵̙͇̗͕̽̀̃̓ ̶̨̧̪̰̥̲͔̳̰͇͙͓͌͆̈́̈̃̕ĭ̸̭͍̜̭̤͎̞̭̰̈́ş̴̧̥̳͉̹͙̓͗͛͂̓͊̃ ̸̡̛͉̮̖͕̯̥̥̘̣̫̬̾͋̾̀̔̓̌̐̀͂͂͘͝w̶̢͎̖͒͌̎̃̔̈̕ĥ̴̨̘͙͍̞͕̝̰̙̟̣̤́̿̐͠ͅā̷̢̪͍͎̻̼͓̥̗̌̎̔̎͐̀̃̈́̍͌͝t̶̨̡̺̻̺̥̮̹̘̮͖͍͖̏̈́̊̎'̵͍̺̾̊̐ş̶͚̖̦̥̯͚͔̬̱͙̦̞̣̩̄͐̈́̃͛̚͘͝ ̴̡̨̢͔̟̦̤̤̤̲͍̹̈̅̃̔͛̾͒̌̑̈̈́̇͝͠͠ÿ̷̡̤̳͇͙͍̼͙́̓̀̏̆̍̀̎̑̑͜o̶̳̖̮͕̲̼̘̭̪̲͍͈͗̀̉͊́̽͜͝͝͝u̸͍͎͙̳͔̬͐̉͑́͠'̶͙̿̈́̅͒̿̉̏̂́̌̕͝r̴̡͙͕̻̮͙̟̫̤͇̼̘̗͕͌͗̿̈͊͐͝e̸͍̳̳̰̺̳̥̮̦͈̦͊̿͒̀̂͆̽̌͘ ̴̥̠̩̦̱̻͆͜ḍ̶̡̦̩̻̓͑̾ͅơ̶̡̠̺͚̯͓̠̬̙͇̦̽͗͒i̶̛͕̻̤͍͈͕̩̐͆͗́̎̿̓͆̀̉̆̀͝͝ṋ̶̤͕͇̦̣̗̩̣͊͛g̸̢̧̯̦͓̬̣̩̱̲͓͓̫̤͊̍͂͒ ̴̧͔̝̗̻͕͉͚͔̜͚͌̅̾̓̃̊̊̇̆̈͘͘̕b̶̡̡̬̺̘̻͚̺̺͑͊̍̒͊̈́̓̃̃ȅ̷͊̄̂ͅs̸̤̻̘̩͇͎̺͕̠͍͉͇͗̅̈̿̾̐̈́̔̈́̚͘͝ͅt̶̢͚͎͚̪̬̝̪͇͈̑̽͂͜ ̴̠̘̯̬̯̱̘̞͙̬͔̎̋̈́?̵̨̛̯͙̰̦̝͇͓̱̯̆̋̍͒̑̑̉̌̃̂͂͘͠͠ͅ")
            print("human part killed")    
            exit()

cyborg = Cyborg('Sandevistan', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.charge()
cyborg.cyberpsychosis()
cyborg.check()
cyborg.cyberpsychosis()
cyborg.add_aliment()
cyborg.cyberpsychosis()
cyborg.eat()
cyborg.cyberpsychosis()
cyborg.digest()
cyborg.cyberpsychosis()
