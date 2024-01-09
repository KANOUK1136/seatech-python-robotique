import time

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """

    def __init__(self, name=None):
	
      if name:
        self.__name = name
      self.__current_state = self.__states[0]
      self.__power = False

    def boot(self):
      self.__power = True
      self.__current_state = self.__states[1]
      pass
	
    def shutdown(self):
      self.__power = False
      self.__current_state = self.__states[0]
      pass
	
    def charge(self):
      for i in range(self.__battery_level,100):
        self.__battery_level = self.__battery_level + 1
        print("charge de la batterie : %d", self.__battery_level)
        time.sleep(0.1) 	
      pass

    
