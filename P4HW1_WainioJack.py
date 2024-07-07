def get_valid_score():
    while True:
        try:
            score = int(input("Enter a score (0-100): "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100. Please try again.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a valid integer score.")

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    num_scores = int(input("Enter the number of scores you want to enter: "))

    scores = []
    for i in range(num_scores):
        valid_score = get_valid_score()
        scores.append(valid_score)

    print("\nScores entered:", scores)

    lowest_score = min(scores)
    print("Lowest score entered:", lowest_score)

    scores.remove(lowest_score)
    print("Score list after dropping lowest score:", scores)

    average_score = calculate_average(scores)
    print(f"Average score: {average_score:.2f}")

    letter_grade = determine_letter_grade(average_score)
    print("Letter grade:", letter_grade)

if __name__ == "__main__":
    main()
