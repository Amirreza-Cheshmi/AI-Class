class Character:
  def __init__(self, name, power, health, coins):
    self.name = name
    self.power = power
    self.health = health
    self.coins = coins
    self.level = 1  

  def show_info(self):
    print(f"Name : {self.name} *** Level : {self.level} *** Power : {self.power} *** Health : {self.health} *** Coins : {self.coins}")

  def is_alive(self):
    return self.health > 0

  def attack(self, x):
    x.health -= self.power
    print( f"{self.name} attacked {x.name}. {x.name}'s health = {x.health}")

  def earn_coins(self, amount):
    self.coins += amount
    print("Coins = ", self.coins)

  def buy_potion(self):
    print(f"{self.name} Health : {self.health}")
    if self.coins >= 20:
      self.coins -= 20
      self.health += 30
      print(f"{self.name} Health (after buy potion) = {self.health}")
    else:
      print("Not enough coins")

  def level_up(self):
    self.level += 1
    self.power += 5
    print(f"{self.name} new level : {self.level}, New power : {self.power}")


player1 = Character("mmd", 50, 1000, 70)
player2 = Character("amir", 70, 1000, 100)

print("show info:")
player1.show_info()
player2.show_info()
print("-"*40)

player1.attack(player2)
player2.attack(player1)
player2.attack(player1)
player2.attack(player1)
player1.attack(player2)


player1.buy_potion()
player2.level_up()

print("-"*40)
print("show info after fight:")

player1.show_info()
player1.is_alive()

player2.show_info()
player2.is_alive()
