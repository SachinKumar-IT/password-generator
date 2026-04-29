import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['+','!','@','#','$','%','&','*','(',')']

print("Welcome to Password Generator!!")
print("Note: For security, your password must contain at least 1 letter, 1 number, and 1 symbol. Minimum total length: 6\n")

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
    """Return strength level (Weak/Medium/Strong) based on length only (as requested)."""
    length = len(password)
    if length < 6:
        strength = "Weak"
        advice = "Password must be at least 6 characters long."
    elif length <= 8:   # 6 to 8 inclusive
        strength = "Medium"
        advice = "Good, but adding more characters (9+) would make it Strong."
    else:               # 9 or more
        strength = "Strong"
        advice = "Excellent password length!"
    return strength, advice

# Loop until user provides valid counts that meet mandatory rules
while True:
    print("--- Enter password composition ---")
    n_letters = get_positive_int("How many letters? ", min_value=1)
    n_numbers = get_positive_int("How many numbers? ", min_value=1)
    n_symbols = get_positive_int("How many symbols? ", min_value=1)
    
    total_length = n_letters + n_numbers + n_symbols
    
    if total_length < 6:
        print(f"Total length is {total_length}. Minimum total length is 6. Please increase one or more categories.\n")
        continue
    else:
        break

# Build the password list
password_list = []

for _ in range(n_letters):
    password_list.append(random.choice(letters))

for _ in range(n_numbers):
    password_list.append(random.choice(numbers))

for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

# Shuffle to randomize order
random.shuffle(password_list)

# Convert to string
password = "".join(password_list)

# Check strength
strength, advice = check_strength(password)

print(f"\n✅ Generated password: {password}")
print(f"🔒 Password strength: {strength}")
print(f"💡 {advice}")
