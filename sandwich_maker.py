
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if ingredient not in self.machine_resources or self.machine_resources[ingredient] < quantity:
                return False
        return True
        
        

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Returns the sandwich when the order can be made, or False if ingredients are insufficient."""
        if self.check_resources(order_ingredients):
            for ingredient in order_ingredients:
                self.machine_resources[ingredient] -= order_ingredients[ingredient]
            return order_ingredients
        else:
            return False
        