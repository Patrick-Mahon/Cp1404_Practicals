
def main():
    score = score_input()
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent score")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def score_input():
    score = float(input("Enter score: "))
    return score

main()
