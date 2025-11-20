"""
Level 2 MONOLITHIC: Add Italian Restaurant (No Pattern)
=======================================================

Now supporting two cuisine types - starting to see the problems.
- Code duplication appearing
- Method names getting cuisine-specific
- Hard to switch between cuisines cleanly
"""


class Restaurant:
    """Restaurant that can serve American or Italian food."""

    def __init__(self, cuisine_type):
        self.cuisine_type = cuisine_type
        if cuisine_type == "American":
            self.name = "American Diner"
        elif cuisine_type == "Italian":
            self.name = "Italian Trattoria"

    def create_american_main(self):
        """Create American main dish."""
        return "Burger (beef patty, lettuce, tomato, pickles)"

    def create_american_side(self):
        """Create American side dish."""
        return "French Fries (crispy, salted)"

    def create_american_drink(self):
        """Create American drink."""
        return "Cola (ice cold, 16oz)"

    def create_italian_main(self):
        """Create Italian main dish."""
        return "Pizza Margherita (mozzarella, tomato, basil)"

    def create_italian_side(self):
        """Create Italian side dish."""
        return "Caesar Salad (romaine, parmesan, croutons)"

    def create_italian_drink(self):
        """Create Italian drink."""
        return "Wine (red, house selection)"

    def serve_meal(self):
        """Serve a complete meal based on cuisine type."""
        print(f"=== Welcome to {self.name} ===\n")

        # Need to check cuisine type for each item
        if self.cuisine_type == "American":
            main = self.create_american_main()
            side = self.create_american_side()
            drink = self.create_american_drink()
        elif self.cuisine_type == "Italian":
            main = self.create_italian_main()
            side = self.create_italian_side()
            drink = self.create_italian_drink()

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
