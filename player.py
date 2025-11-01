
from item import Item
from type import ItemType
from inventory import Inventory
from weapon import Weapon, WeaponSlot
class Player:
    def __init__(self, max_hp:int=100) -> None:
        self.max_hp: int = max_hp
        self.health: int = max_hp
        self.inventory: Inventory = Inventory()
        self.loadout: Loadout = Loadout()
    def take_damage(self, amount:int) -> None:
        self.health = max(0, self.health - amount)
    def heal(self, amount:int) -> None:
        self.health = min(self.max_hp, self.health + amount)    
    def grabs_item(self, item:Item) -> None:
        print(f"Player grabbed {item}")
        self.inventory.add_item(item, 1)
    def get_inventory(self):
        return self.inventory.display_inventory()
    
    
    def equip_item(self, item:Item) -> None:
        if not self.inventory.contains(item):
            print("No such item in inventory")
            return
        if not item.is_equippable():
            print("Item is not equippable")
            return
        print("enter match")
        match item.type:
            case ItemType.HELMET:
                self.loadout.equipped_items["helmet"] = item
                print("helmet equipped")
            case ItemType.CHESTPLATE:
                self.loadout.equipped_items["chestplate"] = item
                print("chestplate equipped")
            case ItemType.BOOTS:
                self.loadout.equipped_items["boots"] = item
                print("boots equipped")
            case ItemType.WEAPON:
                weapon: Weapon = item
                print("weapon enter")
                if weapon.slot == WeaponSlot.TWO_HANDED:
                    self.loadout.equipped_items["off_hand"] = item
                    self.loadout.equipped_items["main_hand"] = item
                    print("2h weapon equipped")
                elif weapon.slot == WeaponSlot.OFF_HAND:
                    self.loadout.equipped_items["off_hand"] = item
                    print("off-hand weapon equipped")
                else:
                    self.loadout.equipped_items["main_hand"] = item
                    print("1h weapon equipped")
                    
    
class Loadout:
    def __init__(self) -> None:
        self.equipped_items: dict[str, Item] = {
            "main_hand": None,
            "off_hand": None,
            "helmet": None,
            "chestplate": None,
            "boots": None,
        }
    
    def unequip_item(self, slot:str) -> None:
        pass
    
    def display_loadout(self) -> None:
        pass

# Example usage
player: Player = Player()
sword: Weapon = Weapon("Iron Sword", 15, "A basic iron sword", 1.2, 1.0, 0.1, 1.5, WeaponSlot.TWO_HANDED)
#player.loadout.equip_item(sword)
player.grabs_item(sword)
player.equip_item(sword)
print(player.loadout.equipped_items)
player.get_inventory()