 # Author = Kiyashko Alexander Maksimovich
 # Group = P3118
 # Date = 10.11.2025
import re

def check_password(password):
    errors = []
    
    if not re.match(r'^.{5,}$', password):
        errors.append("Rule 1 - Your password must be at least 5 characters.")
    
    if not re.search(r'\d', password):
        errors.append("Rule 2 - Your password must include a number.")
    
    if not re.search(r'[A-Z]', password):
        errors.append("Rule 3 - Your password must include an uppercase letter.")
    
    if not re.search(r'[^A-Za-z0-9\s]', password):
        errors.append("Rule 4 - Your password must include a special character.")
    
    digits = re.findall(r'\d', password)
    digit_sum = sum(int(digit) for digit in digits) if digits else 0
    if digit_sum != 25:
        errors.append("Rule 5 - The digits in your password must add up to 25.")
    
    months = r'(january|february|march|april|may|june|july|august|september|october|november|december)'
    if not re.search(months, password, re.IGNORECASE):
        errors.append("Rule 6 - Your password must include a month of the year.")
    
    return errors

def validate_password():
    password = input("Please choose a password: ")
    errors = check_password(password)
    
    if not errors:
        print("✅ All rules passed! Password is valid.")
    else:
        print("❌ Password validation failed:")
        for error in errors:
            print(f"  - {error}")

# Тесты
def run_tests():
    test_cases = [
        {
            "password": "January25!ABCxyz",
            "expected": [],
            "description": "Valid password meeting all rules"
        },
        {
            "password": "Ab1!",
            "expected": ["Rule 1"],
            "description": "Password too short"
        },
        {
            "password": "january25!abc",
            "expected": ["Rule 3"],
            "description": "No uppercase letter"
        },
        {
            "password": "January25ABC",
            "expected": ["Rule 4"],
            "description": "No special character"
        },
        {
            "password": "January10!ABC",
            "expected": ["Rule 5"],
            "description": "Digits sum not 25"
        },
        {
            "password": "ABC25!XYZ123",
            "expected": ["Rule 6"],
            "description": "No month name"
        }
    ]
    
    print("Running tests...")
    for i, test in enumerate(test_cases, 1):
        errors = check_password(test["password"])
        error_rules = [err.split(" - ")[0] for err in errors]
        expected_rules = test["expected"]
        
        if set(error_rules) == set(expected_rules):
            print(f"✅ Test {i} PASSED: {test['description']}")
        else:
            print(f"❌ Test {i} FAILED: {test['description']}")
            print(f"   Expected: {expected_rules}")
            print(f"   Got: {error_rules}")
        print()

if __name__ == "__main__":
    run_tests()

    print("\n" + "="*50)
    validate_password()