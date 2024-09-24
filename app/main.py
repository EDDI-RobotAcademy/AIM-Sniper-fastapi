import os

from fastapi import FastAPI

from openai_api.controller.openai_api_controller import openaiApiRouter

app = FastAPI()

app.include_router(openaiApiRouter)


if __name__ == "__main__":
    import uvicorn
    myIp = os.getenv("MY_IP")
    uvicorn.run(app, host=myIp, port=33333)