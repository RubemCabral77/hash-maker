from src.strategies.base import EncryptorStrategy

class Encryptor:
    def __init__(self, encryptor_strategy: EncryptorStrategy):
        self.encryptor_strategy = encryptor_strategy

    def set_strategy(self, encryptor_strategy: EncryptorStrategy):
        self.encryptor_strategy = encryptor_strategy

    def run(self, data: str) -> str:
        return self.encryptor_strategy.encrypt(data)

