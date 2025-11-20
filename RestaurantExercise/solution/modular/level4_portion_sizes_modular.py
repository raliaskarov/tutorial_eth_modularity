"""
Level 4 MODULAR: Add Portion Sizes (Abstract Factory Pattern)
==============================================================

Adding portion sizes is EASY with Abstract Factory!
- Create Regular and Large versions of each meal factory
- Clean, maintainable, extensible
- No conditionals needed
"""


# American Menu Items - Regular
class Burger:
    """American burger - regular size."""

    def __init__(self):
        self.name = "Burger"
        self.description = "beef patty, lettuce, tomato, pickles"

    def __str__(self):
        return f"{self.name} ({self.description})"


class DoubleBurger:
    """American burger - large size."""

    def __init__(self):
        self.name = "Double Burger"
        self.description = "2 beef patties, lettuce, tomato, pickles, bacon"

    def __str__(self):
        return f"{self.name} ({self.description})"


class FrenchFries:
    """American fries - regular size."""

    def __init__(self):
        self.name = "French Fries"
        self.description = "crispy, salted"

    def __str__(self):
        return f"{self.name} ({self.description})"


class FrenchFriesLarge:
    """American fries - large size."""

    def __init__(self):
        self.name = "French Fries"
        self.description = "crispy, salted, extra large serving"

    def __str__(self):
        return f"{self.name} ({self.description})"


class Cola:
    """American cola - regular size."""

    def __init__(self):
        self.name = "Cola"
        self.description = "ice cold, 16oz"

    def __str__(self):
        return f"{self.name} ({self.description})"


class ColaLarge:
    """American cola - large size."""

    def __init__(self):
        self.name = "Cola"
        self.description = "ice cold, 32oz"

    def __str__(self):
        return f"{self.name} ({self.description})"


# Italian Menu Items - Regular
class Pizza:
    """Italian pizza - regular size."""

    def __init__(self):
        self.name = "Pizza Margherita"
        self.description = "mozzarella, tomato, basil"

    def __str__(self):
        return f"{self.name} ({self.description})"


class PizzaLarge:
    """Italian pizza - large size."""

    def __init__(self):
        self.name = "Pizza Margherita Family Size"
        self.description = "mozzarella, tomato, basil, extra cheese"

    def __str__(self):
        return f"{self.name} ({self.description})"


class CaesarSalad:
    """Italian salad - regular size."""

    def __init__(self):
        self.name = "Caesar Salad"
        self.description = "romaine, parmesan, croutons"

    def __str__(self):
        return f"{self.name} ({self.description})"


class CaesarSaladLarge:
    """Italian salad - large size."""

    def __init__(self):
        self.name = "Caesar Salad"
        self.description = "romaine, parmesan, croutons, grilled chicken"

    def __str__(self):
        return f"{self.name} ({self.description})"


class Wine:
    """Italian wine - regular size."""

    def __init__(self):
        self.name = "Wine"
        self.description = "red, house selection"

    def __str__(self):
        return f"{self.name} ({self.description})"


class WineLarge:
    """Italian wine - large size."""

    def __init__(self):
        self.name = "Wine"
        self.description = "red, premium selection, full bottle"

    def __str__(self):
        return f"{self.name} ({self.description})"


# Mexican Menu Items - Regular
class Tacos:
    """Mexican tacos - regular size."""

    def __init__(self):
        self.name = "Tacos"
        self.description = "seasoned beef, salsa, cilantro, lime"

    def __str__(self):
        return f"{self.name} ({self.description})"


class TacosLarge:
    """Mexican tacos - large size."""

    def __init__(self):
        self.name = "Tacos Platter"
        self.description = "3 tacos, seasoned beef, salsa, cilantro, lime, guacamole"

    def __str__(self):
        return f"{self.name} ({self.description})"


class RefriedBeans:
    """Mexican refried beans - regular size."""

    def __init__(self):
        self.name = "Refried Beans"
        self.description = "pinto beans, spices"

    def __str__(self):
        return f"{self.name} ({self.description})"


class RefriedBeansLarge:
    """Mexican refried beans - large size."""

    def __init__(self):
        self.name = "Refried Beans"
        self.description = "pinto beans, spices, cheese, sour cream"

    def __str__(self):
        return f"{self.name} ({self.description})"


class Horchata:
    """Mexican horchata - regular size."""

    def __init__(self):
        self.name = "Horchata"
        self.description = "rice milk, cinnamon, vanilla"

    def __str__(self):
        return f"{self.name} ({self.description})"


class HorchataLarge:
    """Mexican horchata - large size."""

    def __init__(self):
        self.name = "Horchata"
        self.description = "rice milk, cinnamon, vanilla, 24oz"

    def __str__(self):
        return f"{self.name} ({self.description})"


# Abstract Factory Pattern: Meal Factories
class AmericanRegularMealFactory:
    """Factory for regular American meals."""

    def create_main(self):
        return Burger()

    def create_side(self):
        return FrenchFries()

    def create_drink(self):
        return Cola()


class AmericanLargeMealFactory:
    """Factory for large American meals."""

    def create_main(self):
        return DoubleBurger()

    def create_side(self):
        return FrenchFriesLarge()

    def create_drink(self):
        return ColaLarge()


class ItalianRegularMealFactory:
    """Factory for regular Italian meals."""

    def create_main(self):
        return Pizza()

    def create_side(self):
        return CaesarSalad()

    def create_drink(self):
        return Wine()


class ItalianLargeMealFactory:
    """Factory for large Italian meals."""

    def create_main(self):
        return PizzaLarge()

    def create_side(self):
        return CaesarSaladLarge()

    def create_drink(self):
        return WineLarge()


class MexicanRegularMealFactory:
    """Factory for regular Mexican meals."""

    def create_main(self):
        return Tacos()

    def create_side(self):
        return RefriedBeans()

    def create_drink(self):
        return Horchata()


class MexicanLargeMealFactory:
    """Factory for large Mexican meals."""

    def create_main(self):
        return TacosLarge()

    def create_side(self):
        return RefriedBeansLarge()

    def create_drink(self):
        return HorchataLarge()


class Restaurant:
    """Restaurant that uses a meal factory."""

    def __init__(self, meal_factory, name, portion_size):
        self.meal_factory = meal_factory
        self.name = name
        self.portion_size = portion_size

    def serve_meal(self):
        """Serve a complete meal."""
        main = self.meal_factory.create_main()
        side = self.meal_factory.create_side()
        drink = self.meal_factory.create_drink()

        print(f"=== Welcome to {self.name} ({self.portion_size} Portion) ===\n")
        print(f"Main:  {main}")
        print(f"Side:  {side}")
        print(f"Drink: {drink}")


if __name__ == "__main__":
    print("--- American Regular Meal ---")
    factory = AmericanRegularMealFactory()
    restaurant = Restaurant(factory, "American Diner", "Regular")
    restaurant.serve_meal()

    print("\n--- American Large Meal ---")
    factory = AmericanLargeMealFactory()
    restaurant = Restaurant(factory, "American Diner", "Large")
    restaurant.serve_meal()

    print("\n--- Italian Regular Meal ---")
    factory = ItalianRegularMealFactory()
    restaurant = Restaurant(factory, "Italian Trattoria", "Regular")
    restaurant.serve_meal()

    print("\n--- Mexican Large Meal ---")
    factory = MexicanLargeMealFactory()
    restaurant = Restaurant(factory, "Mexican Cantina", "Large")
    restaurant.serve_meal()
