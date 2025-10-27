from player import Player

def main():
    test_playerHP()
    
def test_playerHP():
    player: Player = Player()
    print(player.health)
    player.take_damage(20)
    print(player.health)
    player.heal(10)
    print(player.health)

if __name__ == "__main__":
    main()
