
def display_menu():
    print("\nGame Inventory Management")
    print("1. Add a Game")
    print("2. Edit a Game")
    print("3. Delete a Game")
    print("4. Search for a Game")
    print("5. Display All Games")
    print("6. Exit")

def add_game(inventory):
    name = input("Enter the name of the game: ").strip()
    link = input("Enter the link to the game: ").strip()
    if name in inventory:
        print("Game already exists in the inventory.")
    else:
        inventory[name] = link
        print(f"Game '{name}' added successfully.")

def edit_game(inventory):
    name = input("Enter the name of the game to edit: ").strip()
    if name in inventory:
        new_name = input(f"Enter the new name for '{name}' (or press Enter to keep the same): ").strip()
        new_link = input(f"Enter the new link for '{name}': ").strip()
        new_name = new_name if new_name else name
        inventory[new_name] = new_link
        if new_name != name:
            del inventory[name]
        print(f"Game '{name}' updated successfully.")
    else:
        print("Game not found.")

def delete_game(inventory):
    name = input("Enter the name of the game to delete: ").strip()
    if name in inventory:
        del inventory[name]
        print(f"Game '{name}' deleted successfully.")
    else:
        print("Game not found.")

def search_game(inventory):
    name = input("Enter the name of the game to search for: ").strip()
    if name in inventory:
        print(f"Game: {name}\nLink: {inventory[name]}")
    else:
        print("Game not found.")

def display_all_games(inventory):
    if inventory:
        print("\nAll Games in Inventory:")
        for name, link in inventory.items():
            print(f"Game: {name}, Link: {link}")
    else:
        print("No games in the inventory.")

def main():
    inventory = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_game(inventory)
        elif choice == "2":
            edit_game(inventory)
        elif choice == "3":
            delete_game(inventory)
        elif choice == "4":
            search_game(inventory)
        elif choice == "5":
            display_all_games(inventory)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
