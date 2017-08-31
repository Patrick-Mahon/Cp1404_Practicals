
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

for state in STATE_NAMES:
    max_length = max((len(state) for state in STATE_NAMES))
    print("{:{}} is {}".format(state, max_length, STATE_NAMES[state]))
