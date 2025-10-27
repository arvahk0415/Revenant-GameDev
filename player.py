from item import Item
class Player:
    def __init__(self, max_hp:int=100) -> None:
        self.max_hp = max_hp
        self.health = max_hp
    def take_damage(self, amount:int) -> None:
        self.health = max(0, self.health - amount)
    def heal(self, amount:int) -> None:
        self.health = min(self.max_hp, self.health + amount)    
    def grabs_item(self, item:Item) -> None:
        print(f"Player grabbed {item}")
    
