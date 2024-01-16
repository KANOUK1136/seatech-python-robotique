import time

class Robot():
    __name = "<unnamed>"
    __power = False
    __action = ''
    __speed = 0
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
    #name
    @property
    def name(self):
      return self.__name
    
    @name.setter
    def name(self, name):
      self.__name = name
    
    #power
    @property
    def power(self):
      return self.__power
    
    @power.setter
    def power(self, power):
      self.__power = power
    
    #battery
    @property
    def battery_level(self):
      return self.__battery_level
    
    @battery_level.setter
    def battery_level(self, battery_level):
      self.__battery_level = battery_level

    #action
    @property
    def action(self):
      return self.__action
    
    @power.setter
    def action(self, action):
      if self.__power:
        self.__action = action

    """
      Give your best code here ( •̀ ω •́ )✧
    """

    def __init__(self, name=None):
	
      if name:
        self.__name = name
      self.__current_state = self.__states[0]
      self.__power = False
      self.__speed = 0

    #boot the robot

    def boot(self):
      if self.__power == False:
        self.__power = True
        self.__current_state = self.__states[1]
        print("ON")
      pass
	
    #shutdown the robot

    def shutdown(self):
      if self.__power == True:
        self.__power = False
        self.__speed = 0
        print("OFF")
      pass
	
    #charge the robot (10 sec for an empty battery)

    def charge(self):
      for i in range(self.__battery_level,100):
        self.__battery_level = self.__battery_level + 1
        print("charge de la batterie : ", self.__battery_level,"%")
        time.sleep(0.1) 
      return self.__battery_level

    #change the speed value to 10

    def move(self):
      if self.__power == True:
        self.__speed = 10
        print("vitesse actuelle : ", self.__speed)
      else:
        print(r1.__name, "is off")
    
    #change the speed value to 0

    def stop(self):
      if self.__power == True:
        self.__speed = 0
        print("vitesse actuelle : ", self.__speed)
      else:
        print(r1.__name, "is off")
    
    #Display the status

    def check(self):
      print("""
system status display
--------------------
""")
      print("name :", self.__name)
      print("battery :", self.__battery_level)
      print("power :", self.__power)
      print("speed :", self.__speed)


#You can use the different method in the main part

if __name__ == '__main__':
  r1 = Robot()
  r1.name = "feur"

  print(r1.battery_level)
  r1.boot()
  r1.charge()
  print(r1.battery_level)
  r1.move()
  r1.stop()
  r1.shutdown()
  r1.check()
  
  

