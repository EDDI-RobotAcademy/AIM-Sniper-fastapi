import os

from fastapi import FastAPI

app = FastAPI()


if __name__ == "__main__":
    import uvicorn
    myIp = os.getenv("MY_IP")
    uvicorn.run(app, host=myIp, port=33333)