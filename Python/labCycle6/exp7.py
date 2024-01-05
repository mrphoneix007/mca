try:
    number = float(input("Enter a number: "))
    if number < 0:
        raise ValueError("Entered number is negative")
    
    print(f"The number entered is: {number}")

except ValueError as e:
    print(f"Error: {e}")
