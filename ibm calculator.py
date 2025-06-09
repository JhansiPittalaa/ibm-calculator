# Continuous BMI Calculator

def calculate_bmi():
    while True:
        print("\n=== BMI CALCULATOR ===")

        name = input("Enter your name: ")
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        bmi = weight / (height ** 2)

        # Determine the BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        # Display the result
        print(f"\n{name}, your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

        # Ask if user wants to calculate again
        repeat = input("\nDo you want to calculate BMI for another person? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you for using the BMI Calculator!")
            break

# Run the BMI calculator
calculate_bmi()
