import time

def show_menu():
    print("=== Fantasy Item Shop ===")
    print("1. buy sword - 50 gold")
    print("2. buy shield - 30 gold")
    print("3. buy potion - 10 gold")
    print("4. buy bow - 40 gold")
    print("5. view inventory")
    print("6. exit shop")
    print("7. sell item")
    print("8. work")
    time.sleep(1)



        
def show_inventory(player_items):
        if not player_items:
            print("Your inventory is empty.")
        for item in player_items:
            print(f"- {item}")
        time.sleep(1)

def can_buy(player_gold, item_cost):
    if player_gold >= item_cost:
        return True
    else:
        print(f"You don't have enough gold to buy this item. You need {item_cost - player_gold} more gold.")
        return False

def buy_item(gold, inventory, item_name, price):
    if can_buy(gold, price) == True:
        gold -= price
        inventory.append(item_name)
        print(f"You bought a {item_name}!")
        print(f"You have {gold} gold left.")
        time.sleep(1)
        return gold
    else:
        print(f"You don't have enough gold to buy a {item_name}.")
        print(f"You have {gold} gold left.")
        time.sleep(1)
        return gold
    
    
def choose_difficulty():
    print("choose the difficulty level:")
    print("1. Easy")
    print("2. normal")
    print("3. Hard")
    difficulty = input("Enter your choice (1-3): ")
    if difficulty == "1":
        print("You have chosen Easy difficulty.")
        gold = 300
        return gold
    elif difficulty == "2":
        print("You have chosen Normal difficulty.")
        gold = 200
        return gold
    elif difficulty == "3":
        print("You have chosen Hard difficulty.")
        gold = 100
        return gold
    else:
        print("Invalid choice. Please choose a valid difficulty level.")
        return choose_difficulty()

def sell_item(gold, inventory):
    for i in range(len(inventory)):
        print(f"{i+1} {inventory[i]}")
    if len(inventory) <1:
        print ("you have nothing")
        time.sleep(1)
    else:
        item = int(input ("wat dou you want to sell"))
        item -= 1
        sell = inventory[item]

        sure = input (f"are you shure you want to sell {sell}")
        sure = sure.lower()
        if sure == 'no':
            print ('nothing was sold')
            return gold
        elif sure == 'yes':

            time.sleep(1)
            if sell == 'sword':
                gold += 25
            elif sure == 'shield':
                gold += 15
            elif sure == 'potion':
                gold += 5
            elif sure == 'bow':
                gold += 20
            inventory.pop(item-1)
            print (gold)
            for i in range(len(inventory)):
                print(f"{i+1} {inventory[i]}")
            return gold
        else:
            print('h,m')

def work(gold):
    for i in range(101):
        print(f"you are {i}% done")
        time.sleep(0.2)
    gold += 20
    print(f"you have {gold} gold")
    time.sleep(1)
    return gold
    


print("Hello Periode 2!")

player_name = input("What is your name? ")
player_gold = choose_difficulty()
player_items = []

print(f"Welcome {player_name}! You have {player_gold} gold and your inventory is empty.")

items_shop = ["sword", "shield", "potion", "bow"]
print("Items available in the shop:")
for item in items_shop:
    print(f"- {item}")

shop_choise = 0
while shop_choise != "6":
    show_menu()
    shop_choise = input("What would you like to do? ")


    
    match shop_choise:
        case "1":
            item_cost = 50
            player_gold = buy_item(player_gold, player_items, "sword", item_cost)
        case "2":
            item_cost = 30
            player_gold = buy_item(player_gold, player_items, "shield", item_cost)
        case "3":
            item_cost = 10
            player_gold = buy_item(player_gold, player_items, "potion", item_cost)
        case "4":
            item_cost = 40
            player_gold = buy_item(player_gold, player_items, "bow", item_cost)
        case "5":
            show_inventory(player_items)
            time.sleep(1)
        case "6":
            print(f"Thank you for visiting the shop, {player_name}")
            print(f"you have {player_gold} left")
            time.sleep(1)
        case "7":
            player_gold = sell_item(player_gold, player_items)
        case "8":
            player_gold = work(player_gold)
        case _:
            print("Invalid choice. Please try again.")
            time.sleep(1)