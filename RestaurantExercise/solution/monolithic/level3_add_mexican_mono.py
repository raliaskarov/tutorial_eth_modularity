"""
Level 3 MONOLITHIC: Add Mexican Cantina (No Pattern)
====================================================

Three cuisine types - the monolithic approach is clearly breaking down.
- 9 different creation methods (3 cuisines × 3 items)
- Lots of if/elif checking
- Error-prone: easy to forget a case
- Very hard to maintain and extend
"""


class Restaurant:
    """Restaurant that can serve American, Italian, or Mexican food."""

    def __init__(self, cuisine_type):
        self.cuisine_type = cuisine_type
        if cuisine_type == "American":
            self.name = "American Diner"
        elif cuisine_type == "Italian":
            self.name = "Italian Trattoria"
        elif cuisine_type == "Mexican":
            self.name = "Mexican Cantina"

    # American menu methods
    def create_american_main(self):
        return "Burger (beef patty, lettuce, tomato, pickles)"

    def create_american_side(self):
        return "French Fries (crispy, salted)"

    def create_american_drink(self):
        return "Cola (ice cold, 16oz)"

    # Italian menu methods
    def create_italian_main(self):
        return "Pizza Margherita (mozzarella, tomato, basil)"

    def create_italian_side(self):
        return "Caesar Salad (romaine, parmesan, croutons)"

    def create_italian_drink(self):
        return "Wine (red, house selection)"

    # Mexican menu methods
    def create_mexican_main(self):
        return "Tacos (seasoned beef, salsa, cilantro, lime)"

    def create_mexican_side(self):
        return "Refried Beans (pinto beans, spices)"

    def create_mexican_drink(self):
        return "Horchata (rice milk, cinnamon, vanilla)"

    def serve_meal(self):
        """Serve a complete meal based on cuisine type."""
        print(f"=== Welcome to {self.name} ===\n")

        # This if/elif chain is getting really long and unmaintainable
        if self.cuisine_type == "American":
            main = self.create_american_main()
            side = self.create_american_side()
            drink = self.create_american_drink()
        elif self.cuisine_type == "Italian":
            main = self.create_italian_main()
            side = self.create_italian_side()
            drink = self.create_italian_drink()
        elif self.cuisine_type == "Mexican":
            main = self.create_mexican_main()
            side = self.create_mexican_side()
            drink = self.create_mexican_drink()
        else:
            # Error handling needed!
            print("ERROR: Unknown cuisine type!")
            return

        print(f"Main:  {main}")
        print(f"Side:  {side}")
        print(f"Drink: {drink}")


if __name__ == "__main__":
    print("--- American Meal ---")
    american_restaurant = Restaurant("American")
    american_restaurant.serve_meal()

    print("\n--- Italian Meal ---")
    italian_restaurant = Restaurant("Italian")
    italian_restaurant.serve_meal()

    print("\n--- Mexican Meal ---")
    mexican_restaurant = Restaurant("Mexican")
    mexican_restaurant.serve_meal()
