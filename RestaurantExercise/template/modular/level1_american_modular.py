"""
Level 1 MODULAR: American Diner (Early Abstract Factory)
=========================================================

Modular version with separate classes for menu items.
- Menu items are separate classes
- Restaurant uses factory methods
- Easier to extend later
"""


class Burger:
    """American burger."""

    def __init__(self):
        self.name = "Burger"
        self.description = "beef patty, lettuce, tomato, pickles"

    def __str__(self):
        return f"{self.name} ({self.description})"


class FrenchFries:
    """American french fries."""

    def __init__(self):
        self.name = "French Fries"
        self.description = "crispy, salted"

    def __str__(self):
        return f"{self.name} ({self.description})"


class Cola:
    """American cola drink."""

    def __init__(self):
        self.name = "Cola"
        self.description = "ice cold, 16oz"

    def __str__(self):
        return f"{self.name} ({self.description})"


class AmericanMealFactory:
    """Factory for creating American meals."""

    def create_main(self):
        """Create main dish."""
        return Burger()

    def create_side(self):
        """Create side dish."""
        return FrenchFries()

    def create_drink(self):
        """Create drink."""
        return Cola()


class Restaurant:
    """Restaurant that uses a meal factory."""

    def __init__(self, meal_factory, name):
        self.meal_factory = meal_factory
        self.name = name

    def serve_meal(self):
        """Serve a complete meal."""
        main = self.meal_factory.create_main()
        side = self.meal_factory.create_side()
        drink = self.meal_factory.create_drink()

        print(f"=== Welcome to {self.name} ===\n")
        print(f"Main:  {main}")
        print(f"Side:  {side}")
        print(f"Drink: {drink}")


if __name__ == "__main__":
    factory = AmericanMealFactory()
    restaurant = Restaurant(factory, "American Diner")
    restaurant.serve_meal()
