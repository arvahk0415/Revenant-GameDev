from item import Item
from inventory import Inventory
class Player:
    def __init__(self, max_hp:int=100, inventory:Inventory=Inventory()) -> None:
        self.max_hp = max_hp
        self.health = max_hp
        self.inventory = inventory
    def take_damage(self, amount:int) -> None:
        self.health = max(0, self.health - amount)
    def heal(self, amount:int) -> None:
        self.health = min(self.max_hp, self.health + amount)    
    def grabs_item(self, item:Item) -> None:
        print(f"Player grabbed {item}")
        self.inventory.add_item(item, 1)
    
