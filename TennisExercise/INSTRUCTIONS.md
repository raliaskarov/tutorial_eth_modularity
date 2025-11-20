# Tennis Scoring System - Exercise

**Pattern**: Facade
**Goal**: Learn how Facade provides a simple interface to complex subsystems

## What We're Building
A tennis scoring system that tracks player scores and displays them correctly. As we add features (tennis terminology, win tracking, multi-language support), you'll see how the Facade pattern keeps the interface simple while managing growing complexity.

## Quick Start
1. Level 1 is provided as working starter code
2. Implement levels 2-4 in both `template/monolithic/` and `template/modular/`
3. Compare your solutions with `solution/` when done

---

## Level 1: Player Names

**Requirements**:
- Two players with names
- Track numeric scores (0, 1, 2, 3, 4...)
- Score points for players by name
- Display current score
- Detect when game is over (score >= 4)
- Reset game functionality

**Example**:
```
Alice: 1, Bob: 0
Alice: 2, Bob: 1
Game Over! Winner: Alice
```

**Status**: ✓ Provided as starter code

---

## Level 2: Tennis Terminology

**New Requirements**:
- Use official tennis scores: "love", "fifteen", "thirty", "forty"
- Display tied scores as "love all", "fifteen all", etc.
- Scores >= 4 display as numbers

**Example**:
```
Alice: fifteen, Bob: love
Alice: thirty, Bob: love
Game: Alice
```

---

## Level 3: Track Games Won

**New Requirements**:
- Track total games won for each player
- Display games won in parentheses: `(1-0)`, `(1-1)`
- Games won persist when game resets

**Example**:
```
Game: Alice (1-0)
Game: Bob (1-1)
```

---

## Level 4: Multi-Language Support

**New Requirements**:
- Support English and German languages
- German terms: "null", "fünfzehn", "dreißig", "vierzig", "Spiel", "beide"
- Add `set_language()` method to switch languages

**Example (German)**:
```
Spiel: Alice (1-0)
```
