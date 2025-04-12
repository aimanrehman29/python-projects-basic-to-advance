import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
    "user@example.com": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",  # "hello" hashed
    "anotheruser@example.com": "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8e7b19e5768c14680d0d11327",  # "password" hashed
}

new_email = "newuser@example.com"
new_password = "newpassword"
stored_logins[new_email] = hash_password(new_password) 

def login(email, password_to_check):
    """
    Takes an email and a password, hashes the password_to_check, 
    and checks it against the stored password hash for that email.
    Returns True if the hashes match, False otherwise.
    """
    password_to_check = password_to_check.strip()

    hashed_password_to_check = hash_password(password_to_check)

    if email in stored_logins and stored_logins[email] == hashed_password_to_check:
        return True
    return False

email = input("Enter your email: ")
password = input("Enter your password: ")

if login(email, password):
    print("Login successful!")
else:
    print("Login failed. Incorrect email or password.")
