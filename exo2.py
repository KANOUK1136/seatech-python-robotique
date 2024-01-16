from exo1 import Robot

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


cyborg = Cyborg('Sandevistan', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.charge()
cyborg.check()
cyborg.add_aliment()
cyborg.eat()
cyborg.digest()
print("sexe :", cyborg.sexe)

# cyborg.truc_fun()