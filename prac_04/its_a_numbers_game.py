def main():
    numbers = []
    amounts = 0

    while amounts != 5:
        number = int(input("Number: "))
        numbers.append(number)
        amounts = amounts + 1
    print("The first number is: ", numbers[0])
    print("The last number is: ", numbers[4])
    print("The smallest number is: ", min(numbers))
    print("The largest number is: ", max(numbers))
    print("The average number is: ", sum(numbers)/5)

main()