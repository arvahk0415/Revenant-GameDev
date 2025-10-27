from player import Player, Item
from type import ItemType

def main() -> None:
    test_playerHP()
    
def test_playerHP() -> None:
    player: Player = Player()
    print(player.health)
    player.take_damage(20)
    print(player.health)
    player.heal(10)
    print(player.health)
    
    item: Item = Item("Potion", "This is a test item.", ItemType.CONSUMABLE)
    player.grabs_item(item)
    print(item.is_equippable())

if __name__ == "__main__":
    main()
