"""
Level 3 MODULAR: Add Mexican Cantina (Abstract Factory Pattern)
================================================================

Adding Mexican is trivial with Abstract Factory.
- Just create new Mexican menu items
- Create MexicanMealFactory
- No changes to existing code!
"""


# American Menu Items
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


# Italian Menu Items
class Pizza:
    """Italian pizza."""

    def __init__(self):
        self.name = "Pizza Margherita"
        self.description = "mozzarella, tomato, basil"

    def __str__(self):
        return f"{self.name} ({self.description})"


class CaesarSalad:
    """Italian salad."""

    def __init__(self):
        self.name = "Caesar Salad"
        self.description = "romaine, parmesan, croutons"

    def __str__(self):
        return f"{self.name} ({self.description})"


class Wine:
    """Italian wine."""

    def __init__(self):
        self.name = "Wine"
        self.description = "red, house selection"

    def __str__(self):
        return f"{self.name} ({self.description})"


# Mexican Menu Items
class Tacos:
    """Mexican tacos."""

    def __init__(self):
        self.name = "Tacos"
        self.description = "seasoned beef, salsa, cilantro, lime"

    def __str__(self):
        return f"{self.name} ({self.description})"


class RefriedBeans:
    """Mexican refried beans."""

    def __init__(self):
        self.name = "Refried Beans"
        self.description = "pinto beans, spices"

    def __str__(self):
        return f"{self.name} ({self.description})"


class Horchata:
    """Mexican horchata drink."""

    def __init__(self):
        self.name = "Horchata"
        self.description = "rice milk, cinnamon, vanilla"

    def __str__(self):
        return f"{self.name} ({self.description})"


# Abstract Factory Pattern: Meal Factories
class AmericanMealFactory:
    """Factory for creating American meals."""

    def create_main(self):
        return Burger()

    def create_side(self):
        return FrenchFries()

    def create_drink(self):
        return Cola()


class ItalianMealFactory:
    """Factory for creating Italian meals."""

    def create_main(self):
        return Pizza()

    def create_side(self):
        return CaesarSalad()

    def create_drink(self):
        return Wine()


class MexicanMealFactory:
    """Factory for creating Mexican meals."""

    def create_main(self):
        return Tacos()

    def create_side(self):
        return RefriedBeans()

    def create_drink(self):
        return Horchata()


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
    print("--- American Meal ---")
    american_factory = AmericanMealFactory()
    american_restaurant = Restaurant(american_factory, "American Diner")
    american_restaurant.serve_meal()

    print("\n--- Italian Meal ---")
    italian_factory = ItalianMealFactory()
    italian_restaurant = Restaurant(italian_factory, "Italian Trattoria")
    italian_restaurant.serve_meal()

    print("\n--- Mexican Meal ---")
    mexican_factory = MexicanMealFactory()
    mexican_restaurant = Restaurant(mexican_factory, "Mexican Cantina")
    mexican_restaurant.serve_meal()
