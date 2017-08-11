import inventory as inventory

class player(object):
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp
    self.inv = inventory()
    
  def move(self, dir):
    pass
  
  def attack(self, enemy):
    pass
  
 
