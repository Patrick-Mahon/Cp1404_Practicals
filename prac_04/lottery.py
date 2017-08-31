
import random

number_on_line = 6
min = 1
max = 45

def main():
    amount_of_quick_picks = int(input("Enter quick picks here: "))

    for i in range(amount_of_quick_picks):
        quick_picks = []
        for o in range(number_on_line):
            number = random.randint(min, max)
            while number in quick_picks:
                number = random.randint(min, max)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))

main()