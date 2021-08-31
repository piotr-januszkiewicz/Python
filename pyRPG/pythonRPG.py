#idea: modern rpg. a person living in present reality

#Lets start with smth classical: name, money and hp. based on that
#I can start building a story
class Player:
    def __init__(self, Name, Money, HealthPoints):
        self.name = Name
        self.money = Money
        self.hp = HealthPoints
        
    def spend_money(self, amount):
        self.money -= amount

    def lose_health(self, amount):
        self.hp -= amount

class Choices:
    def __init__(self):
        self.choices = []

    def get_choice(self, pos):
        if pos <= len(choices):
            return self.choices[pos]
        else: return None

   
