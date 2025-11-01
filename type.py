from enum import Flag, auto

class ItemType(Flag):
    #ARMOR TYPES
    HELMET = auto()
    CHESTPLATE = auto()
    BOOTS = auto()
    ARMOR = HELMET | CHESTPLATE | BOOTS
    
    #WEAPON TYPES
    ONE_HANDED = auto()
    TWO_HANDED = auto()
    OFF_HAND = auto()

    #WEAPON SUBTYPES
    SWORD = auto()
    BOW = auto()
    MAGIC_STAFF = auto()
    WEAPON = SWORD | BOW | MAGIC_STAFF
    
    #OTHER TYPES
    CONSUMABLE = auto()
    MATERIAL = auto()

class ElementType(Flag):
    #ELEMENTAL TYPES
    FIRE = auto()             #Chance to cause BURN debuff
    FROST = auto()            #Chance to cause CHILL debuff
    ELECTRIC = auto()         #Chance to cause SHOCK debuff
    TOXIN = auto()            #Chance to cause POISON debuff

    NONE = auto()

class Debuff(Flag):

    #ELEMENTAL EFFECTS
    BURN = auto()             #Takes damage over time, infinitely stacks and resets duration on application.
    CHILL = auto()            #Slightly reduced movement speed and attack speed, freeze at 5 stacks.
    SHOCK = auto()            #Briefly stuns target. Chance to jump to nearby targets. Does not stack, 3 second cooldown on unique targets.
    POISON = auto()           #Takes damage over time, infinite stacks but does not reset duration on application.
    FROZEN = auto()           #Immobilized for duration. Take increased critical damage for duration.
    
    #OTHER DEBUFFS
    SURPRESSED = auto()       #Reduces damage dealt by percentage.
    EXPOSED = auto()          #Increases damage taken by percentage.
    BLEEDING = auto()         #Takes damage over time. Ignores armor.
    
    #STAT DEBUFFS
    WEAKENED = auto()         #Reduces attack damage.
    CRIPPLED = auto()         #Reduces attack speed.
    SUNDERED = auto()         #Reduces armor value.
    SLOWED = auto()           #Reduced movement speed for duration.
    
    NONE = auto()

class CrowdControl(Flag):
    #CROWD CONTROL EFFECTS
    STUNNED = auto()          #Completely unable to act for duration.
    ROOTED = auto()           #Unable to move for duration.
    CONFUSED = auto()         #Random movement and attack direction for duration.
    SILENCED = auto()         #Unable to use abilities for duration.
    BLINDED = auto()          #Chance to miss attacks for duration.
    SLEEP = auto()            #Unable to act until taking damage.
    
    NONE = auto()

class Buff(Flag):

    #ELEMENTAL RESIST
    BURN_RESIST = auto()      #Reduces chance to be inflicted with BURN debuff
    CHILL_RESIST = auto()     #Reduces chance to be inflicted with CHILL debuff
    SHOCK_RESIST = auto()     #Reduces chance to be inflicted with SHOCK debuff
    POISON_RESIST = auto()    #Reduces chance to be inflicted with POISON debuff

    #STAT BUFFS
    STRENGTHENED = auto()     #Increases attack damage value.
    FORTIFIED = auto()        #Increases armor value.
    SWIFT = auto()            #Increases attack speed.
    HASTE = auto()            #Increases movement speed.  

    #OTHER BUFFS
    REGENERATION = auto()     #Heals over time.
    EMPOWERED = auto()        #Increases damage dealt by percentage.
    PROTECTED = auto()        #Reduces damage taken by percentage.

    NONE = auto()
