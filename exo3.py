from abc import ABCMeta, abstractmethod

class Vehicule (metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def Start(self):
        pass
    

class UnderWater_Vehicule (metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def Dive(self):
        pass

class Aerial_Vehicule (metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def Fly(self):
        pass
    

class Ground_Vehicule (metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def Race(self):
        pass
    

class Unmanned(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def do_mission(self):
        pass

class UAV(Unmanned, Aerial_Vehicule):
    def __init__(self): 
        print("Unmanned")
        print("Aerial")
        print("Vehicule")
    
    def Start(self):
        print("Starting")

    def Fly(self):
        print("Fly")

    def do_mission(self):
        self.Start()
        self.Fly()
        print("Mission done")

class UUV(Unmanned, UnderWater_Vehicule):
    def __init__(self): 
        print("Unmanned")
        print("Underwater")
        print("Vehicule")
    
    def Start(self):
        print("Starting")

    def Dive(self):
        print("Diving")

    def do_mission(self):
        self.Start()
        self.Dive()
        print("Mission done")


class UGV(Unmanned, Ground_Vehicule):
    def __init__(self):   
        print("Unmanned")
        print("Ground")
        print("Vehicule")
    
    def Start(self):
        print("Starting")

    def Race(self):
        print("Race")

    def do_mission(self):
        self.Race()
        self.Start()
        print("Mission done")


print("""
    UGV
      """)
ugv = UGV()
ugv.do_mission()

print("""
    UAV
      """)
uav = UAV()
uav.do_mission()

print("""
    UUV
      """)
uuv = UUV()
uuv.do_mission()

    
