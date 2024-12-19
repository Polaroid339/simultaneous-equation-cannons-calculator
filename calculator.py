from itertools import product
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_combinations(total_cards, opponent_value):
    """
    Find valid combinations of Fusion and Xyz monsters for activation.
    :param total_cards: Total number of cards in play (hands + field).
    :param opponent_value: The level or class of the opponent's monster.
    :return: List of valid combinations.
    """
    # Definition of monsters in the Extra Deck
    fusion_levels = [1, 2, 3, 4, 5]  # Levels of Fusion monsters (1 of each)
    xyz_classes = [2, 3, 4, 5, 6]  # Classes of Xyz monsters (2 of each)

    # Generate all possible combinations of 1 Fusion and 2 Xyz monsters (with the same class)
    combinations = product(fusion_levels, xyz_classes)

    # Validate combinations
    valid_combinations = []
    for fusion_level, xyz_class in combinations:
        # Calculate the combined total of Fusion level and Xyz classes (same class for both Xyz)
        combined_total = fusion_level + 2 * xyz_class
        if combined_total == total_cards:
            # Check if we can match the opponent's monster value with returned monsters
            if fusion_level + xyz_class == opponent_value:
                valid_combinations.append((fusion_level, xyz_class))

    return valid_combinations

def display_results(combinations):
    """
    Display the results of valid combinations.
    :param combinations: List of valid combinations.
    """
    if combinations:
        print("Valid combinations to activate the effect:\n")
        for fusion, xyz in combinations:
            print(f"- Banish: 2 Xyz (Class {xyz}), Fusion (Level {fusion})")
            print(f"  Return to Extra Deck: Xyz (Class {xyz}), Fusion (Level {fusion}), \n")
    else:
        print("No valid combinations found for the given requirements.\n")

# Main loop
clear_screen()
print("Welcome to Simultaneous Equation Cannons Calculator\n")
while True:
    try:
        # User input
        total_cards = int(input("Enter the total number of cards in play (hands + field): "))
        opponent_value = int(input("Enter the level/class of an opponent's monster: "))
        clear_screen()

        # Find and display valid combinations
        combinations = find_combinations(total_cards, opponent_value)
        display_results(combinations)

    except ValueError:
        print("\nPlease enter valid numeric inputs.")
