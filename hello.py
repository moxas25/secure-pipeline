# app.py

import os
import random
import math
import string
import hashlib
import json

# 1. Data Manipulation: Convert a dictionary to a sorted JSON string
def dict_to_sorted_json(data):
    return json.dumps(data, sort_keys=True)

# 2. Mathematical Operation: Calculate the greatest common divisor (GCD)
def calculate_gcd(a, b):
    return math.gcd(a, b)

# 3. Random String Generator: Create a random alphanumeric string of given length
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# 4. Hashing Function: Generate SHA-256 hash of a given string
def generate_sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# 5. File Operation: Write a string to a file and read it back
def write_and_read_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    
    with open(filename, 'r') as file:
        return file.read()

# 6. Security Risk: Function with a hardcoded API key (for SAST testing)
def get_api_key():
    api_key = "hardcodedapikey123"  # Hardcoded API key (security risk)
    return api_key

# 7. Main Function
def main():
    print("Sorted JSON: ", dict_to_sorted_json({"b": 2, "a": 1, "c": 3}))
    print("GCD of 56 and 98: ", calculate_gcd(56, 98))
    print("Random String: ", generate_random_string(12))
    print("SHA-256 Hash: ", generate_sha256_hash("Hello, World!"))
    
    filename = "testfile.txt"
    content = "This is a sample file content."
    print("File Content: ", write_and_read_file(filename, content))
    
    print("API Key: ", get_api_key())

if __name__ == "__main__":
    main()
