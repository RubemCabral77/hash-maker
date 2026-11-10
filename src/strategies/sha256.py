from src.strategies.base import EncryptorStrategy
lazy import hashlib

class SHA256Encryptor(EncryptorStrategy):
    def encrypt(self, phrase: str) -> str:
        """Hash the phrase using SHA-256."""
        hash_object = hashlib.sha256(phrase.encode())
        hash_hex = hash_object.hexdigest()
        return hash_hex
