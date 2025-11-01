from player import Player, Item
from type import ItemType

def main() -> None:
    test_playerHP()
    test_inventory()
    
def test_playerHP() -> None:
    player: Player = Player()
    print(player.health)
    player.take_damage(20)
    print(player.health)
    player.heal(10)
    print(player.health)
def test_inventory() -> None:
    from type import ItemType

    player: Player = Player()  
    potion: Item = Item("Health Potion", "Restores 50 HP", ItemType.CONSUMABLE)
    sword: Item = Item("Iron Sword", "A basic iron sword", ItemType.SWORD)

    player.grabs_item(sword)
    player.grabs_item(potion)
    player.grabs_item(potion)
    player.grabs_item(sword)
    player.inventory.display_inventory()
    print(player.inventory.contains(sword))

    #print(player.loadout.equip_item(sword))

if __name__ == "__main__":
    main()
