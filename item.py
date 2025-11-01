from type import ItemType
class Item:
    def __init__(self, name: str, description: str, type: ItemType) -> None:
        self.name: str = name
        self.description: str = description
        self.type: ItemType = type

    def __str__(self) -> str:
        return f"{self.name} ({self.type.name})"
    
    def is_stackable(self) -> bool:
        return self.type == ItemType.CONSUMABLE or self.type == ItemType.MATERIAL

    def is_equippable(self) -> bool:
        return self.type in ItemType.ARMOR or self.type in ItemType.WEAPON
    
    def is_usable(self) -> bool:
        return self.type == ItemType.CONSUMABLE
    
