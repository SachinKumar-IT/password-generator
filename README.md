# 🔐 Secure Password Generator – Python

A **robust password generator** that guarantees each password contains:

- ✅ **At least one uppercase letter**  
- ✅ **At least one lowercase letter**  
- ✅ **At least one number**  
- ✅ **At least one symbol** (special character)  
- ✅ **Total length ≥ 6 characters**  

The final password is **randomly shuffled** to avoid predictable patterns.  
Password strength is assessed purely by length (as requested):

| Length     | Strength |
|------------|----------|
| < 6        | Weak (won't happen due to validation) |
| 6 – 8      | Medium  |
| 9+         | Strong  |

## 🚀 Usage

**Sample Example**
 ```bash
Welcome to Password Generator!!
Note: For security, your password must contain at least 1 uppercase, 1 lowercase, 1 number, and 1 symbol. Minimum total length: 6

--- Enter password composition ---
How many letters? (minimum 2 to include both cases) 2
How many numbers? 1
How many symbols? 1
Total length is 4. Minimum total length is 6. Please increase one or more categories.

--- Enter password composition ---
How many letters? (minimum 2 to include both cases) 3
How many numbers? 2
How many symbols? 1

✅ Generated password: aB3@cD
🔒 Password strength: Medium
💡 Good, but adding more characters (9+) would make it Strong.
  
 **Clone** the repository:
   ```bash
   git clone https://github.com/SachinKumar-IT/password-generator.git
