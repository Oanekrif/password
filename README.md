# 🔑✨ Random Password Generator 🔒💻</br></br></br>

## 📋 Project Description:
This is a simple **Python script** that generates a **random password** with a mix of lowercase,
uppercase, numbers, and special characters.</br>

---

## 🛠️ How It Works:
1. The user inputs the desired **password length**.
2. The script randomly selects characters from:
   - Lowercase letters (`a-z`)</br>
   - Uppercase letters (`A-Z`)</br>
   - Numbers (`0-9`)</br>
   - Special characters (`-!@#$%^&*()_+?[]"|<>`)
3. The final password is displayed.

## 🚀 How to Run:
1. Make sure you have **Python** installed on your system.
2. Clone the repository:
    ```bash
   clone https://github.com/Oanekrif/password.git
3. Navigate to the project directory:
    ```bash
   cd password
4. Run the game script:
    ```bash
    python password.py
5. Enter the password length when prompted.

## 🖥️ Example Output:

    enter length of password: 12
    password dyalek howa: X8@v#R1y!T^p

## 🔧 Code:
Here is the code used in the script:</br>

    import random
    length = input("enter length of password: ")
    password = ''
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_char = '1234567890-!@#$%^&*()_+?[]"|<>'
    for i in range(int(length)):
       random_char = random.choice(lowercase + uppercase + special_char)
       password = password + random_char
    print("password dyalek howa: "+password)

<img src="https://github.com/Oanekrif/password/blob/master/image.png" width="800">
## 📌 Notes:
•Make sure you enter a valid integer for the password length.</br>
•The generated password is a combination of characters to ensure randomness.</br>
•This is a great starting script for learning how to generate passwords in Python.

## 🎉 Enjoy Secure Passwords!
Keep your accounts secure with strong, random passwords! 🔒
