from random import randint

NUMBER_OF_DICE_ROLLS = 100


def main():
    dice_rolls = []

    for _ in range(NUMBER_OF_DICE_ROLLS + 1):
        dice_rolls.append(randint(1, 6))

    numbers_dice_roll = set(dice_rolls)
    sorted(numbers_dice_roll)

    print(f"Foram realizados {NUMBER_OF_DICE_ROLLS} lançamentos.")
    for number in numbers_dice_roll:
        occurrences = dice_rolls.count(number)
        percentage = round((occurrences / len(dice_rolls)) * 100, 2)
        print(f"O número {number} saiu {occurrences} - {percentage}%")


if __name__ == "__main__":
    main()
