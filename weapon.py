from item import Item
from type import ItemType
from enum import Enum, auto

class WeaponSlot(Enum):
    ONE_HANDED = auto()
    TWO_HANDED = auto()
    OFF_HAND = auto()
    
class Weapon(Item):
    def __init__(self, name:str, damage:int, description:str, attack_speed:float, attack_range:float,
                 crit_chance:float, crit_damage:float, slot:WeaponSlot, type:ItemType = ItemType.WEAPON) -> None:
        super().__init__(name, description, type)
        self.damage: int = damage
        self.attack_speed: float = attack_speed
        self.attack_range: float = attack_range
        self.crit_chance: float = crit_chance
        self.crit_damage: float = crit_damage
        self.slot: WeaponSlot = slot
    
    def __str__(self) -> str:
        return f"{self.name} ({self.type.name})"
    



