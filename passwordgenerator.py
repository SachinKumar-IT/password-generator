import random

uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['+','!','@','#','$','%','&','*','(',')']

print("Welcome to Password Generator!!")
print("Note: For security, your password must contain at least 1 uppercase, 1 lowercase, 1 number, and 1 symbol. Minimum total length: 6\n")

def get_positive_int(prompt, min_value=0):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter a number greater than or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_strength(password):
    length = len(password)
    if length < 6:
        strength = "Weak"
        advice = "Password must be at least 6 characters long."
    elif length <= 8:
        strength = "Medium"
        advice = "Good, but adding more characters (9+) would make it Strong."
    else:
        strength = "Strong"
        advice = "Excellent password length!"
    return strength, advice

while True:
    print("--- Enter password composition ---")
    n_letters = get_positive_int("How many letters? (minimum 2 to include both cases) ", min_value=2)
    n_numbers = get_positive_int("How many numbers? ", min_value=1)
    n_symbols = get_positive_int("How many symbols? ", min_value=1)
    
    total_length = n_letters + n_numbers + n_symbols
    if total_length < 6:
        print(f"Total length is {total_length}. Minimum total length is 6. Please increase one or more categories.\n")
        continue
    else:
        break

password_list = []

# Force at least ONE uppercase and ONE lowercase
password_list.append(random.choice(uppercase_letters))
password_list.append(random.choice(lowercase_letters))

# Remaining letters (if any) from combined pool
remaining_letters = n_letters - 2
if remaining_letters > 0:
    all_letters = uppercase_letters + lowercase_letters
    for _ in range(remaining_letters):
        password_list.append(random.choice(all_letters))

# Numbers and symbols
for _ in range(n_numbers):
    password_list.append(random.choice(numbers))
for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

# Shuffle and create final password
random.shuffle(password_list)
password = "".join(password_list)

strength, advice = check_strength(password)

print(f"\n✅ Generated password: {password}")
print(f"🔒 Password strength: {strength}")
print(f"💡 {advice}")
