"""
Level 4 MONOLITHIC: Add Portion Sizes (No Pattern)
==================================================

Adding portion sizes to three cuisines - COMPLETE CHAOS!
- Would need 18 methods (3 cuisines × 3 items × 2 sizes)
- OR nested if/elif checking portion size within cuisine checking
- Combinatorial explosion
- Completely unmaintainable
"""


class Restaurant:
    """Restaurant that can serve American, Italian, or Mexican food in Regular or Large portions."""

    def __init__(self, cuisine_type, portion_size="Regular"):
        self.cuisine_type = cuisine_type
        self.portion_size = portion_size

        if cuisine_type == "American":
            self.name = "American Diner"
        elif cuisine_type == "Italian":
            self.name = "Italian Trattoria"
        elif cuisine_type == "Mexican":
            self.name = "Mexican Cantina"

    # Instead of 18 separate methods, we use nested conditionals
    # This is still terrible but more compact than having 18 methods!

    def create_main(self):
        """Create main dish based on cuisine and portion."""
        if self.cuisine_type == "American":
            if self.portion_size == "Regular":
                return "Burger (beef patty, lettuce, tomato, pickles)"
            else:  # Large
                return "Double Burger (2 beef patties, lettuce, tomato, pickles, bacon)"
        elif self.cuisine_type == "Italian":
            if self.portion_size == "Regular":
                return "Pizza Margherita (mozzarella, tomato, basil)"
            else:  # Large
                return "Pizza Margherita Family Size (mozzarella, tomato, basil, extra cheese)"
        elif self.cuisine_type == "Mexican":
            if self.portion_size == "Regular":
                return "Tacos (seasoned beef, salsa, cilantro, lime)"
            else:  # Large
                return "Tacos Platter (3 tacos, seasoned beef, salsa, cilantro, lime, guacamole)"

    def create_side(self):
        """Create side dish based on cuisine and portion."""
        if self.cuisine_type == "American":
            if self.portion_size == "Regular":
                return "French Fries (crispy, salted)"
            else:  # Large
                return "French Fries (crispy, salted, extra large serving)"
        elif self.cuisine_type == "Italian":
            if self.portion_size == "Regular":
                return "Caesar Salad (romaine, parmesan, croutons)"
            else:  # Large
                return "Caesar Salad (romaine, parmesan, croutons, grilled chicken)"
        elif self.cuisine_type == "Mexican":
            if self.portion_size == "Regular":
                return "Refried Beans (pinto beans, spices)"
            else:  # Large
                return "Refried Beans (pinto beans, spices, cheese, sour cream)"

    def create_drink(self):
        """Create drink based on cuisine and portion."""
        if self.cuisine_type == "American":
            if self.portion_size == "Regular":
                return "Cola (ice cold, 16oz)"
            else:  # Large
                return "Cola (ice cold, 32oz)"
        elif self.cuisine_type == "Italian":
            if self.portion_size == "Regular":
                return "Wine (red, house selection)"
            else:  # Large
                return "Wine (red, premium selection, full bottle)"
        elif self.cuisine_type == "Mexican":
            if self.portion_size == "Regular":
                return "Horchata (rice milk, cinnamon, vanilla)"
            else:  # Large
                return "Horchata (rice milk, cinnamon, vanilla, 24oz)"

    def serve_meal(self):
        """Serve a complete meal."""
        print(f"=== Welcome to {self.name} ({self.portion_size} Portion) ===\n")
        print(f"Main:  {self.create_main()}")
        print(f"Side:  {self.create_side()}")
        print(f"Drink: {self.create_drink()}")


if __name__ == "__main__":
    print("--- American Regular Meal ---")
    Restaurant("American", "Regular").serve_meal()

    print("\n--- American Large Meal ---")
    Restaurant("American", "Large").serve_meal()

    print("\n--- Italian Regular Meal ---")
    Restaurant("Italian", "Regular").serve_meal()

    print("\n--- Mexican Large Meal ---")
    Restaurant("Mexican", "Large").serve_meal()
