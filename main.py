import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    machine = SandwichMaker(resources)
    
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")
        # Add an indented block of code here

        if choice == "off":
            break

        elif choice == "report":
            for ingredient, quantity in sandwich_maker_instance.machine_resources.items(): 
                if ingredient in ["bread", "ham"]:
                    unit = "slice(s)"
                else:
                    unit = "pound(s)"
                print(f"{ingredient}: {quantity} {unit}")

        elif choice in ["small", "medium", "large"]:
            sandwich_size = choice
            order_ingredients = recipes[sandwich_size]["ingredients"]

            if sandwich_maker_instance.check_resources(order_ingredients):
                print("Please insert coins.")
                coins = cashier_instance.process_coins()
                cost = recipes[sandwich_size]["cost"]

                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients)
                    print(f"{sandwich_size} sandwich is ready. Bon appetit!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                for ingredient, quantity in sandwich_maker_instance.machine_resources.items():
                    if quantity <= 0:
                        print(f"Sorry there is not enough {ingredient}.")

if __name__=="__main__":
    main()
