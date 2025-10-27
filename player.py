class Player:
    def __init__(self, max_hp:int=100):
        self.max_hp = max_hp
        self.health = max_hp
    def take_damage(self, amount:int):
        self.health = max(0, self.health - amount)
    def heal(self, amount:int):
        self.health = min(self.max_hp, self.health + amount)    
    
    
