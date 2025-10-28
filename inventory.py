from item import Item

# Inventory class to manage a collection of items
class Inventory:
    def __init__(self) -> None:
        self.items: list[dict] = []
    
    # Adds an item to the inventory
    def add_item(self, item: Item, quantity: int) -> None:
        if quantity <= 0:
            return
        
        # Stackable items: increase quantity if already present
        if item.is_stackable():
            for entry in self.items:
                # Adds quantity to existing entry
                if entry['item'].name == item.name:
                    entry['quantity'] += quantity
                    break
            else:
                # Adds new entry if not found
                self.items.append({'item': item, 'quantity': quantity})
            print(f"--Added {item.name} x{quantity} to inventory--")
        
        # Non-stackable items: add separate entries
        else:
            for _ in range(quantity):
                self.items.append({'item': item, 'quantity': 1})
                print(f"--Added {item.name} to inventory--")
    
    # TODO:
    # Removes a specific quantity of an item from the inventory
    def drop(self, item: Item, quantity: int) -> None:
        pass
    
    # TODO:
    #Removes the entire stack of an item
    def drop_all(self) -> None:
        pass

    # Displays the inventory contents
    def display_inventory(self) -> None:
        print("\n-------Inventory-------")
        display: list = []
        for entry in self.items:
            if entry['quantity'] > 1:
                display.append(f"{entry['item'].name} x{entry['quantity']}")
            else:
                display.append(f"{entry['item'].name}")
        
        print(", ".join(display), end="\n\n")


# Example usage
from type import ItemType
new = Inventory()
potion = Item("Health Potion", "Restores 50 HP", ItemType.CONSUMABLE)
sword = Item("Iron Sword", "A basic iron sword", ItemType.SWORD)

new.add_item(sword, 2)
new.add_item(potion, 3)
new.display_inventory()
new.add_item(potion, 2)
new.add_item(sword, 1)
new.display_inventory()

