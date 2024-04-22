class InvalidNameError(Exception):
    pass
class InvalidAgeError(Exception):
    pass

def validate_voting_eligibility(name, age):
    try:
        if not name.isalpha():
            raise InvalidNameError("Name should contain only alphabets")

        age = int(age)
        if age < 18:
            raise InvalidAgeError("Age should be 18 or above to cast a vote")

        print(f"Congratulations, {name}! You are eligible to cast your vote.")

    except InvalidNameError as e:
        print(f"Invalid name: {e}")
    except InvalidAgeError as e:
        print(f"Invalid age: {e}")
    except ValueError:
        print("Invalid age input. Please enter a valid numeric age.")

name = input("Enter your name: ")
age = input("Enter your age: ")

validate_voting_eligibility(name, age)
