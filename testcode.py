import os
import hashlib

def insecure_password_storage(password):
    # Insecure password storage using MD5 (weak hashing algorithm)
    hash_object = hashlib.md5(password.encode())
    return hash_object.hexdigest()

def hardcoded_secret():
    # Hardcoded API key (sensitive data exposure)
    api_key = "12345-SECRET-API-KEY-67890"
    return api_key

def sql_injection_example(user_input):
    # Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    print(f"Executing query: {query}")

def main():
    # Example usage
    password = "mypassword123"
    print(f"Insecure hashed password: {insecure_password_storage(password)}")

    secret = hardcoded_secret()
    print(f"Hardcoded API key: {secret}")

    user_input = input("Enter your username: ")
    sql_injection_example(user_input)

if __name__ == "__main__":
    main()
