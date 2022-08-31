import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    #uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ["PORT"]))
    # Env 설정을 통해 port 번호를 입력하지 않고 os에서 불러와서 동작하도록 한다.