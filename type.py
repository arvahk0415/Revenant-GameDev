from enum import Flag, auto

class ItemType(Flag):
    #ARMOR TYPES
    HELMET = auto()
    CHESTPLATE = auto()
    BOOTS = auto()
    ARMOR = HELMET | CHESTPLATE | BOOTS
    
    #WEAPON TYPES
    SWORD = auto()
    BOW = auto()
    MAGIC_STAFF = auto()
    WEAPON = SWORD | BOW | MAGIC_STAFF
    
    #OTHER TYPES
    CONSUMABLE = auto()
    MATERIAL = auto()