from abc import ABC, abstractmethod


class OpenaiApiService(ABC):
    @abstractmethod
    def chatWithGpt(self, userSendMessage):
        pass