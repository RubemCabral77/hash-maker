from abc import ABC, abstractmethod

class EncryptorStrategy(ABC):
    @abstractmethod
    def encrypt(self, data: str) -> str:
        pass
