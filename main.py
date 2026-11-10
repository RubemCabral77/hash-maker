from src.encryptor import Encryptor
from src.strategies.sha256 import SHA256Encryptor

if __name__ == "__main__":
    phrase = input("Enter a phrase to hash: ")

    executor = Encryptor(SHA256Encryptor())
    hashed_phrase = executor.run(phrase)

    print(f"Hashed phrase: {hashed_phrase}")
