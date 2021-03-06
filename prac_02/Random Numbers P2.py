import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 1.0
DAY = 0

out_file = open("OUTPUT_FILE.txt", 'w')

price = INITIAL_PRICE
print("Starting Price: ${:,.2f}".format(price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
        DAY = DAY + 1
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
        DAY = DAY + 1
    price *= (1 + price_change)
    print("Day ", DAY, ": ${:,.2f}".format(price), file=out_file)
out_file.close()
