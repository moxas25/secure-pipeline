import os
import hashlib
import sqlite3

# Hard-coded credentials (kwetsbaarheid)
USERNAME = "admin"
PASSWORD = "SuperSecret123"

def insecure_hash(password):
    """Gebruik van een verouderde hashing-methode (MD5)"""
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(user, pwd):
    if user == USERNAME and insecure_hash(pwd) == insecure_hash(PASSWORD):
        print("Authenticated!")
    else:
        print("Authentication failed!")

def store_user_data(user, pwd):
    """Kwetsbare database-opslag zonder encryptie"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pwd))
    conn.commit()
    conn.close()
    print("User data stored.")

if __name__ == "__main__":
    # Simuleer login en opslag
    user_input = input("Enter username: ")
    pwd_input = input("Enter password: ")
    authenticate(user_input, pwd_input)
    store_user_data(user_input, pwd_input)
