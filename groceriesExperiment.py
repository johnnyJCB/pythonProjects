"""In this programming challenge, you are tasked with creating a simple grocery list management program. The program will present the user with three options: entering '0' to shut 
down the program, '1' to add items to the grocery list, or '2' to remove items from the list. If the user chooses to add items, they can input grocery items until they enter 'done' 
to finish. The program will then display the current contents of the grocery list. On the other hand, if the user chooses to remove items, they can input items to remove until they 
enter 'done' to finish. The program will notify the user if the item is not found in the list. Finally, the program will display the sorted final grocery list."""

def grocery_list_challenge():
    print("Enter 0 to shut down, 1 to add items, or 2 to remove items from your groceries list")
    choice = int(input("Your choice: ")) 
    groceries = []  # list store items
    if choice == 0:
        print("Shutting down")
    elif choice == 1:       # add item the user enters "done"
        print("Add items to your groceries list:")
        while True:
            item = input("Enter an item (or 'done' to finish): ")  # user input
            if item.lower() == "done":
                break  # Exit loop "done"
            else:
                groceries.append(item)  # Add the item to list
                print("Current groceries list:", groceries)  # Print current list
    else:
        print("Remove items from your groceries list:")
        while True:
            item = input("Enter an item to remove (or 'done' to finish): ")  # user input
            if item.lower() == "done":
                break  
            else:
                if item in groceries:
                    groceries.remove(item)
                    print("Current groceries list:", groceries)  # Print current list
                else:
                    print("Item not found in the groceries list.")  # item not in list

    print("Final groceries list:", groceries)


if __name__ == "__main__":
    grocery_list_challenge()
