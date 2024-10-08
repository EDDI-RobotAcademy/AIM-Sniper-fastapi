FROM arm64v8/python:3.9

WORKDIR /app

COPY . .

RUN git submodule update --init --recursive

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY svr.crt ./svr.crt
COPY svr.key ./svr.key
COPY CA.pem ./CA.pem

EXPOSE 33333 37373

CMD ["sh", "-c", "python3 -m app.main"]