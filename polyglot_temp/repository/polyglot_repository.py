from abc import ABC, abstractmethod


class PolyglotRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass