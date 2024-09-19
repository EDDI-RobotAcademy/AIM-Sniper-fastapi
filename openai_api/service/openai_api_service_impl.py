from openai_api.repository.openai_api_repository_impl import OpenaiApiRepositoryImpl
from openai_api.service.openai_api_service import OpenaiApiService


class OpenaiApiServiceImpl(OpenaiApiService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__openaiApiRepositoryImpl = OpenaiApiRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def chatWithGpt(self, userSendMessage):
        print(f"service -> chatWithGpt")
        return await self.__openaiApiRepositoryImpl.generateText(userSendMessage)