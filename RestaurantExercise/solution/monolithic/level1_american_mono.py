"""
Level 1 MONOLITHIC: American Diner Only (No Pattern)
====================================================

Simple restaurant with hardcoded American menu items.
- Only serves American food
- Everything in one class
- Works fine for a single cuisine type
"""


class Restaurant:
    """Restaurant that serves American food."""

    def __init__(self):
        self.name = "American Diner"

    def create_main(self):
        """Create main dish."""
        return "Burger (beef patty, lettuce, tomato, pickles)"

    def create_side(self):
        """Create side dish."""
        return "French Fries (crispy, salted)"

    def create_drink(self):
        """Create drink."""
        return "Cola (ice cold, 16oz)"

    def serve_meal(self):
        """Serve a complete meal."""
        print(f"=== Welcome to {self.name} ===\n")
        print(f"Main:  {self.create_main()}")
        print(f"Side:  {self.create_side()}")
        print(f"Drink: {self.create_drink()}")


if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.serve_meal()
