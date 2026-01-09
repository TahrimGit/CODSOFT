print("===== Welcome to Calculator =====")

while True:
    n = int(input("\nEnter first number: "))
    m = int(input("Enter second number: "))

    while True:
        print("\nSelect Operation to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter choice (1/2/3/4): "))

        if choice == 1:
            print("Addition of", n, "and", m, "is:", n + m)

        elif choice == 2:
            print("Subtraction of", n, "and", m, "is:", n - m)

        elif choice == 3:
            print("Multiplication of", n, "and", m, "is:", n * m)

        elif choice == 4:
            if m != 0:
                print("Division of", n, "and", m, "is:", n / m)
            else:
                print("Error! Division by zero.")

        else:
            print("Invalid choice! Try again.")
            continue

        repeat = input("\nDo you want another operation with same numbers? (yes/no): ").lower()
        if repeat != "yes":
            break

    repeat1 = input("\nDo you want to change numbers and continue? (yes/no): ").lower()
    if repeat1 != "yes":
        break

print("\nThank you for using the calculator!")
