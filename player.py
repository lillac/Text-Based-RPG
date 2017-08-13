from inventory import inventory

class player(object):
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp
    self.inv = inventory()

  def isAlive(self):
      return self.hp > 0

  def attack(self, enemy):
    if (enemy.isAlive() == False):
        return 'You cant attack a dead ' + enemy.name
    weapon = self.inv.bestWeapon()
    print('You use ' + weapon.name + ' against ' + enemy.name + ' and do ' + str(weapon.attack) + ' damage!')
    enemy.hp -= weapon.attack
    return enemy.hp
