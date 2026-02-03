from fastapi import FastAPI
from posts.post_api import router as post_router

app = FastAPI()
app.include_router(post_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def hello():
    return "Hello World!"


@app.get("/hi")
def hi():
    return ["hello", "world", "!"]


@app.get("/odd")
def odd():
    result = []
    for i in range(100):
        if i % 2 == 0:
            result.append(i)

    return result
