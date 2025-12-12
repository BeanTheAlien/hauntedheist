from schedule import Skd

class Person:
  def __init__(self, name: str):
    self.__name: str = name
    self.__food: float = 100
    self.__water: float = 100
    self.__skd: list[Skd] = []
    self.__state: int = 0
  
  def feed(self, amount: float) -> float:
    self.__food += amount
    return self.__food
  def starve(self, amount: float) -> float:
    self.__food -= amount
    return self.__food
  def skdAdd(self, entry: Skd) -> list[Skd]:
    self.__skd.append(entry)
    return self.__skd
  def skdRem(self, entry: Skd) -> list[Skd]:
    self.__skd.remove(entry)
    return self.__skd
  
  def name(self) -> str:
    """
    Returns the name of the person.
    
    :param self: This person.
    :return: The name.
    :rtype: str
    """
    return self.__name
  def food(self) -> float:
    """
    Returns the current percent food level of the person.
    
    :param self: This person.
    :return: The food level.
    :rtype: float
    """
    return self.__food
  def water(self) -> float:
    """
    Returns the current percent water level of the person.
    
    :param self: This person.
    :return: The water level.
    :rtype: float
    """
    return self.__water
  def skd(self) -> list[Skd]:
    return self.__skd
  def die(self):
    # need implementation within unreal (nitro python runtime could work)
    self.__state = 1
    print("dead")
  
  def upd(self):
    if self.__state == 1: return
    elif self.__food <= 0 or self.__water <= 0:
      self.die()

  def __str__(self):
    return f"-- Person --\nName: \"{self.__name}\"\nFood: {self.__food}\nWater: {self.__water}"

person = Person("Hello World")
print(person)
person.starve(100)
person.upd()