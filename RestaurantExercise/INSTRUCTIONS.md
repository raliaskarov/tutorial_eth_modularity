# Restaurant Menu System - Exercise

**Pattern**: Abstract Factory
**Goal**: Learn how Abstract Factory manages families of related objects

## What We're Building
A multi-cuisine restaurant system where each cuisine (American, Italian, Mexican) serves matching sets of main dish, side, and drink. As we add cuisines and portion sizes, you'll see how Abstract Factory prevents mixing incompatible items and handles combinatorial complexity cleanly.

## Quick Start
1. Level 1 is provided as working starter code
2. Implement levels 2-4 in both `template/monolithic/` and `template/modular/`
3. Compare your solutions with `solution/` when done

---

## Level 1: American Diner

**Requirements**:
- Serve American-style meals
- Menu: Burger, French Fries, Cola
- Display complete meal with descriptions

**Example**:
```
=== Welcome to American Diner ===

Main:  Burger (beef patty, lettuce, tomato, pickles)
Side:  French Fries (crispy, salted)
Drink: Cola (ice cold, 16oz)
```

**Status**: ✓ Provided as starter code

---

## Level 2: Add Italian Restaurant

**New Requirements**:
- Support American AND Italian cuisines
- Italian menu: Pizza Margherita, Caesar Salad, Wine
- Customer can order from either cuisine

**Example**:
```
=== Welcome to Italian Trattoria ===

Main:  Pizza Margherita (mozzarella, tomato, basil)
Side:  Caesar Salad (romaine, parmesan, croutons)
Drink: Wine (red, house selection)
```

---

## Level 3: Add Mexican Cantina

**New Requirements**:
- Support American, Italian, AND Mexican cuisines
- Mexican menu: Tacos, Refried Beans, Horchata
- Customer can order from any of the three cuisines

**Example**:
```
=== Welcome to Mexican Cantina ===

Main:  Tacos (seasoned beef, salsa, cilantro, lime)
Side:  Refried Beans (pinto beans, spices)
Drink: Horchata (rice milk, cinnamon, vanilla)
```

---

## Level 4: Add Portion Sizes

**New Requirements**:
- Support Regular and Large portions for all cuisines
- Large portions have enhanced items (e.g., Double Burger, extra large fries, 32oz cola)
- Customer can choose any combination of cuisine and portion size

**Example**:
```
=== Welcome to American Diner (Large Portion) ===

Main:  Double Burger (2 beef patties, lettuce, tomato, pickles, bacon)
Side:  French Fries (crispy, salted, extra large serving)
Drink: Cola (ice cold, 32oz)
```
