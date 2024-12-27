# Yu-Gi-Oh! Simultaneous Equation Cannons Calculator

This project provides a Python script to validate card combinations for Simultaneous Equation Cannons Calculator card effect. The script determines valid combinations of Fusion and Xyz monsters from the Extra Deck to meet the seccond effect condition.
<br>
<div align="center">
  <img src="https://static.wikia.nocookie.net/yugioh/images/2/2e/SimultaneousEquationCannons-LEDE-EN-C-1E.png/revision/latest?cb=20240429230120" alt="Yu-Gi-Oh Card" width="300">
</div>
<br>


>Banish 1 Fusion Monster and 2 Xyz Monsters with the same Rank from your Extra Deck, whose combined Level and Ranks equal the total number of cards in both player's hands and on the field, then you can apply this effect.
>
>Return 2 of your banished monsters to the Extra Deck (1 Xyz and 1 Fusion) whose combined Level and Rank equal the Level or Rank of 1 face-up monster your opponent controls, then banish all cards they control.



## Features
- Calculates valid combinations of monsters based on:
  - Total number of cards in play (hands and field).
  - The level/class of an opponent's monster.
- Ensures the Xyz monsters have the same class when banished.
- Displays detailed information about the combinations to assist with game strategy.
- Provides a clear and interactive interface for input and results.

## Requirements
- Python 3.x
- Flet library
- Itertools library
- Compatible with Windows, macOS, and Linux.

## How It Works
1. **Input Requirements:**
   - Total number of cards in play (both players' hands and field).
   - Level or class of an opponent's monster.

2. **Processing:**
   - The script iterates over predefined levels of Fusion monsters and classes of Xyz monsters.
   - Validates combinations where:
     - The sum of levels and classes matches the total number of cards.
     - The combination allows returning monsters to match the opponent's monster.

3. **Output:**
   - Displays all valid combinations for the given inputs.
   - Specifies which monsters to banish and which to return to the Extra Deck.

## Usage
1. Clone the repository or download the script.
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
2. Run the script:
   
   ```
   flet run main.py
   ```
4. Follow the on-screen prompts to input the required values.
5. View the results, showing valid combinations or an error message if none are found.

Or simply run the Simultaneous Equation Cannons Calculator.exe, but the program is based on my extra deck which contain 1 Fusion monster from level 1 to 5, and Xyz monsters from class 2 to 6, 2 of each.

## Example
### Input:
```
Enter the total number of cards in play: 10
Enter the level/class of an opponent's monster: 7
```
### Output:
```
Valid combinations to activate the effect:

- Banish: 2 Xyz (Class 3), Fusion (Level 4)
- Return to Extra Deck: Xyz (Class 3), Fusion (Level 4)
```

## Customization
You can modify the `fusion_levels` and `xyz_classes` lists in the script to match your deck's configuration.

then build you app: 
```
flet pack main.py --name "Simultaneous Equation Cannons Calculator"
```

## Notes
- Ensure that the inputs provided are integers and correspond to valid game scenarios.
- The script does not simulate gameplay; it only validates specific card logic.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contribution
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.
