# Kaun Banega Crorepati

print("Welcome to Kaun Banega Crorepati\n")
print("Let the fun begin...\n")

# Question 1
print("1. What is the capital city of France?")
print("a. Lyon")
print("b. Paris")
print("c. Nantes")
print("d. Nice")
ans1 = input("Enter your answer: ").lower()

if ans1 == "b":
    print("\nCongratulations! You won 500\n")

    # Question 2
    print("2. How many days are there in a week?")
    print("a. 7")
    print("b. 8")
    print("c. 5")
    print("d. 6")
    ans2 = input("Enter your answer: ").lower()

    if ans2 == "a":
        print("\nCongratulations! You won 1000\n")

        # Question 3
        print('3. Which animal is known as the "King of the Jungle"?')
        print("a. Tiger")
        print("b. Lion")
        print("c. Peacock")
        print("d. Dinosaur")
        ans3 = input("Enter your answer: ").lower()

        if ans3 == "b":
            print("\nCongratulations! You won 2000\n")

            # Question 4
            print("4. How many legs does a spider have?")
            print("a. 9")
            print("b. 10")
            print("c. 8")
            print("d. 12")
            ans4 = input("Enter your answer: ").lower()

            if ans4 == "c":
                print("\nCongratulations! You won 4000\n")

                # Question 5
                print("5. Which planet do we live on?")
                print("a. Jupiter")
                print("b. Earth")
                print("c. Mars")
                print("d. Pluto")
                ans5 = input("Enter your answer: ").lower()

                if ans5 == "b":
                    print("\nCongratulations! You won 8000\n")

                    # Question 6
                    print("6. Which ocean is the largest in the world?")
                    print("a. Pacific Ocean")
                    print("b. Indian Ocean")
                    print("c. Antarctic Ocean")
                    print("d. Arabian Ocean")
                    ans6 = input("Enter your answer: ").lower()

                    if ans6 == "a":
                        print("\nCongratulations! You won 16000\n")
                    else:
                        print("\nWrong answer. You won 8000 only.")
                else:
                    print("\nWrong answer. You won 4000 only.")
            else:
                print("\nWrong answer. You won 2000 only.")
        else:
            print("\nWrong answer. You won 1000 only.")
    else:
        print("\nWrong answer. You won 500 only.")
else:
    print("\nBetter luck next time!")