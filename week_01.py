import time
print("Hello Periode 2!")

player_name = input("What is your name? ")
player_gold = 100
player_items = []

print(f"Welcome {player_name}! You have {player_gold} gold and your inventory is empty.")

items_shop = ["sword", "shield", "potion", "bow"]
print("Items available in the shop:")
for item in items_shop:
    print(f"- {item}")

shop_choise = 0
while shop_choise != "6":
    print("=== Fantasy Item Shop ===")
    print("1. buy sword - 50 gold")
    print("2. buy shield - 30 gold")
    print("3. buy potion - 10 gold")
    print("4. buy bow - 40 gold")
    print("5. view inventory")
    print("6. exit shop")
    time.sleep(1)

    shop_choise = input("What would you like to do? ")
    
    match shop_choise:
        case "1":
            if player_gold >= 50:
                player_gold -= 50
                player_items.append("sword")
                print("You bought a sword!")
                print(f"You have {player_gold} gold left.")
            else:
                print("You don't have enough gold to buy a sword.")
            time.sleep(1)
        case "2":
            if player_gold >= 30:
                player_gold -= 30
                player_items.append("shield")
                print("You bought a shield!")
                print(f"You have {player_gold} gold left.")
            else:
                print("You don't have enough gold to buy a shield.")
            time.sleep(1)
        case "3":
            if player_gold >= 10:
                player_gold -= 10
                player_items.append("potion")
                print("You bought a potion!")
                print(f"You have {player_gold} gold left.")
            else:
                print("You don't have enough gold to buy a potion.")
            time.sleep(1)
        case "4":
            if player_gold >= 40:
                player_gold -= 40
                player_items.append("bow")
                print("You bought a bow!")
                print(f"You have {player_gold} gold left.")
            else:
                print("You don't have enough gold to buy a bow.")
            time.sleep(1)
        case "5":
            print("Your inventory:")
            if not player_items:
                print("Your inventory is empty.")
            for item in player_items:
                print(f"- {item}")
            time.sleep(1)
        case "6":
            print(f"Thank you for visiting the shop, {player_name}")
            print(f"you have {player_gold} left")
            time.sleep(1)
        case _:
            print("Invalid choice. Please try again.")
            time.sleep(1)