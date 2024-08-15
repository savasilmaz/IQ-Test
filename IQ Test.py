def start_test():
    print("Welcome to the Progressive Intelligence Test!")
    print("This test consists of several questions designed to estimate your IQ.")
    print("The difficulty will increase with each question.")
    print("Type 'Start' when you're ready to begin.")

    start = input("> ").strip().lower()
    if start == 'start':
        play_game()
    else:
        print("You need to type 'Start' to begin the test!")


def play_game():
    score = 0

    # 1st Question
    print("\n1st Question: 1, 1, 2, 3, 5, 8, 13, ? What is the next number in the series?")
    print("a) 20\nb) 21\nc) 22\nd) 23")
    answer1 = input("> ").strip().lower()
    if answer1 == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was b) 21.")

    # 2nd Question
    print("\n2nd Question: Which shape does not belong to this series? Circle, Square, Triangle, Rectangle")
    print("a) Circle\nb) Square\nc) Triangle\nd) Rectangle")
    answer2 = input("> ").strip().lower()
    if answer2 == "a":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was a) Circle.")

    # 3rd Question
    print("\n3rd Question: 6, 24, 60, 120, ?, 336 What number should fill the gap in this series?")
    print("a) 180\nb) 210\nc) 240\nd) 300")
    answer3 = input("> ").strip().lower()
    if answer3 == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was b) 210.")

    # 4th Question (Revised)
    print("\n4th Question: There are 10 rabbits in a garden. Each rabbit gives birth to 10 rabbits every 10 days.")
    print("The newborn rabbits also start giving birth 10 days after they are born.")
    print("How many rabbits will there be at the end of 30 days?")
    print("a) 1100\nb) 3310\nc) 12310\nd) 13310")
    answer4 = input("> ").strip().lower()
    if answer4 == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was c) 12310.")

    # 5th Question (Difficult level)
    print("\n5th Question: How many times do the hour and minute hands of a clock overlap in a day?")
    print("a) 22\nb) 23\nc) 24\nd) 12")
    answer5 = input("> ").strip().lower()
    if answer5 == "a":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was a) 22.")

    # Results
    print("\nThe test is over! Your score:", score)
    if score == 5:
        print("Congratulations! You have a very high IQ!")
    elif 3 <= score < 5:
        print("Well done! You have an above-average IQ.")
    else:
        print("It looks like you need more practice.")


if __name__ == "__main__":
    start_test()

