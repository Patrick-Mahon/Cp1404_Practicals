import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
DAY = 0

price = INITIAL_PRICE
print("Starting Price: ${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0

    if random.randint(1, 2) == 1:

        price_change = random.uniform(0, MAX_INCREASE)
        DAY = DAY + 1
    else:

        price_change = random.uniform(-MAX_DECREASE, 0)
        DAY = DAY + 1
    price *= (1 + price_change)
    print("Day ", DAY, ": ${:,.2f}".format(price))