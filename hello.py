# hello_world.py
import os

def hello_world(name):
    """
    Function that returns a greeting message
    """
    return f"Hello, {name}!"

def secret_function():
    """
    A function that simulates a secret being hardcoded in the code
    """
    api_key = "my-secret-api-key-12345"
    print(f"API Key: {api_key}")

if __name__ == "__main__":
    name = os.getenv("USER_NAME", "World")  # Using environment variable or default value
    print(hello_world(name))
    secret_function()  # Simulates a secret in code
